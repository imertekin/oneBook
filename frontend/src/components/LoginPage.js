import { Formik, Form, Field, ErrorMessage} from "formik";
import * as Yup from "yup";
import axios from "axios";

export default function LoginPage({ setIsLoggin }) {
  let errormsg = "";

  const handleOnSubmit = async (values, actions) => {
    try {
      const res = await axios.post("http://127.0.0.1:8000/api/token/", {
        username: values.username,
        password: values.password,
      });
      localStorage.setItem("access_token", res.data.access);
      localStorage.setItem("refresh_token", res.data.refresh);
      setIsLoggin(true);
      window.location.href = "/";
    } catch (error) {
      error.response.status === 401 &&
        (errormsg = <>Username or Password Wrong</>);
    }
  };

  return (
    <div className="login-container">
      <Formik
        initialValues={{
          username: "",
          password: "",
        }}
        validationSchema={Yup.object({
          username: Yup.string().required("Username required"),
          password: Yup.string()
            .min(5, "Too short !")
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
              <Field
                id="username"
                type="text"
                placeholder="Username"
                value={values.username}
                onChange={handleChange}
                onblur={handleBlur}
              />

                 <ErrorMessage name="username" />

              <Field
                id="password"
                type="password"
                placeholder="Password"
                value={values.password}
                onChange={handleChange}
                onblur={handleBlur}
              />
              <ErrorMessage name="password" />

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
