import { Formik, Form } from "formik";
import * as Yup from "yup";
import axios from "axios";


export default function RegisterPage({setIsLoggin}) {

    const handleOnSubmit= async(values,actions)=>{
        try {
            await axios.post("http://127.0.0.1:8000/api/register/",
            {username:values.username,
            password:values.password,
            password2:values.password2,
            email:values.email,
            first_name:values.first_name,
            last_name:values.last_name
        })
        const loggin = await axios.post("http://127.0.0.1:8000/api/token/",
        {username:values.username,
        password:values.password})
        localStorage.setItem('access_token', loggin.data.access);
        localStorage.setItem('refresh_token', loggin.data.refresh);
        setIsLoggin(true)
        window.location.href = '/'
        

          } catch (error) {
        
    }}


    return (
        <div className="login-container registerU">
      <Formik
        initialValues={{
          username: "",
          password: "",
          password2:"",
          email:"",
          first_name:"",
          last_name:"",
        }}
        validationSchema={Yup.object({
          username: Yup.string().required("Username Required"),
          password: Yup.string()
            .min(5, "Too Short!")
            .required("Password required"),
        password2:Yup.string()
        .required("Password required")
        .oneOf(
            [Yup.ref("password")],
            "Both password need to be the same"
          ),
          email:Yup.string()
          .required("Password required")
          .email(),
          
        first_name:  Yup.string()
        .required("first name required"),

        last_name:  Yup.string()
        .required("last name required")

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
        }) => {
          return (
              
            <Form>
                <img src="assets\images\monster.png" alt="Logo" />
                <input
                  id="username"
                  type="text"
                  placeholder="Username"
                  value={values.username}
                  onChange={handleChange}
                />
                {errors.username && touched.username && (
                  <div>{errors.username}</div>
                )}
                <input
                  id="password"
                  type="password"
                  placeholder="Password"
                  value={values.password}
                  onChange={handleChange}
                />
                {errors.password && touched.password && (
                  <div>{errors.password}</div>
                )}
                <input
                  id="password2"
                  type="password"
                  placeholder="Password confirm"
                  value={values.password2}
                  onChange={handleChange}
                />
                <input
                  id="email"
                  type="email"
                  placeholder="Email"
                  value={values.email}
                  onChange={handleChange}
                />
                <input
                  id="first_name"
                  type="text"
                  placeholder="First Name"
                  value={values.first_name}
                  onChange={handleChange}
                />
                <input
                  id="last_name"
                  type="text"
                  placeholder="Last Name"
                  value={values.last_name}
                  onChange={handleChange}
                />

                <button type="submit" disabled={!dirty || isSubmitting}>
                  Register
                </button>
            </Form>
          );
        }}
      </Formik>
    </div>
    )
}
