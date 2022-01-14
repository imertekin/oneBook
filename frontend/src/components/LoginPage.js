import { Formik, Form,ErrorMessage } from "formik";
import * as Yup from "yup";
import axios from "axios";

export default function LoginPage({setIsLoggin}) {

    let errormsg=''

    const handleOnSubmit= async(values,actions)=>{
        try {
            const res = await axios.post("http://127.0.0.1:8000/api/token/",
            {username:values.username,
            password:values.password})
            localStorage.setItem('access_token', res.data.access);
            localStorage.setItem('refresh_token', res.data.refresh);
            setIsLoggin(true)
            window.location.href = '/'
          } catch (error) {
          error.response.status===401&& (
            errormsg=<>Username or Password Wrong</>
          )
        
    }}

  return (
    <div className="login-container">
      <Formik
        initialValues={{
          username: "",
          password: "",
        }}
        validationSchema={Yup.object({
          username: Yup.string().required("Username Required"),
          password: Yup.string()
            .min(5, "Too Short!")
            .required("Password required"),
        })}
        onSubmit={handleOnSubmit}
      >
        {({
          values,
          errors,
          touched,
          handleChange,
          handleSubmit,
          dirty,
          isSubmitting,
          handleBlur,
        }) => {
          return (
              
            <Form>
                <img src="assets\images\monster.png" alt="Logo" />
                {errormsg}
                <input
                  id="username"
                  type="text"
                  placeholder="Username"
                  value={values.username}
                  onChange={handleChange}
                  onBlur={handleBlur}
                  
                />
                
                {errors.username && touched.username && (
                  <div style={{color:"red",fontSize:"15px"}}>{errors.username}</div>
                )}
                
                
                <input
                  id="password"
                  type="password"
                  placeholder="Password"
                  value={values.password}
                  onChange={handleChange}
                  onBlur={handleBlur}
                />
                {errors.password && touched.password && (
                  <div>{errors.password}</div>
                )}

                <button type="submit" disabled={!dirty || isSubmitting}>
                  Login
                </button>
            </Form>
          );
        }}
      </Formik>
    </div>
  );
}
