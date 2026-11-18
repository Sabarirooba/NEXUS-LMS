import streamlit as st

st.set_page_config(
    page_title="NEXUS LMS",
    page_icon="🎓",
    layout="wide"
)

# Session State Initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = ""

if "username" not in st.session_state:
    st.session_state.username = ""


# -----------------------------------
# LOGIN FUNCTION
# -----------------------------------

def login_page():

    st.title("🎓 NEXUS LMS")
    st.subheader("AI Powered Learning Management System")

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
        width=150
    )

    st.markdown("---")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    role = st.selectbox(
        "Select Role",
        ["Student", "Instructor", "Admin"]
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login", use_container_width=True):

            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = role

            st.success("Login Successful")

            st.rerun()

    with col2:
        if st.button("Forgot Password", use_container_width=True):
            st.session_state.page = "forgot"
            st.rerun()

    st.markdown("---")

    if st.button("New Student Registration"):
        st.session_state.page = "register"
        st.rerun()


# -----------------------------------
# REGISTRATION PAGE
# -----------------------------------

def registration_page():

    st.title("📝 Student Registration")

    with st.form("registration"):

        fullname = st.text_input("Full Name")

        email = st.text_input("Email")

        mobile = st.text_input("Mobile Number")

        qualification = st.selectbox(
            "Qualification",
            [
                "B.Sc",
                "BCA",
                "B.Com",
                "B.E",
                "MCA",
                "MBA"
            ]
        )

        username = st.text_input("Create Username")

        password = st.text_input(
            "Create Password",
            type="password"
        )

        submit = st.form_submit_button("Register")

        if submit:

            st.success("Registration Successful ✅")

            st.balloons()

    if st.button("Back To Login"):
        st.session_state.page = "login"
        st.rerun()


# -----------------------------------
# FORGOT PASSWORD PAGE
# -----------------------------------

def forgot_password():

    st.title("🔐 Forgot Password")

    email = st.text_input("Registered Email")

    if st.button("Send Reset Link"):
        st.success(
            f"Password reset link sent to {email}"
        )

    if st.button("Back To Login"):
        st.session_state.page = "login"
        st.rerun()


# -----------------------------------
# USER PROFILE
# -----------------------------------

def profile_page():

    st.title("👤 User Profile")

    st.write("Username:", st.session_state.username)

    st.write("Role:", st.session_state.role)

    st.write("Email:", "sample@gmail.com")

    st.write("Phone:", "9876543210")

    st.write("Qualification:", "BCA")

    if st.button("Edit Profile"):
        st.session_state.page = "edit"
        st.rerun()


# -----------------------------------
# EDIT PROFILE
# -----------------------------------

def edit_profile():

    st.title("✏ Edit Profile")

    name = st.text_input(
        "Name",
        "John Student"
    )

    mobile = st.text_input(
        "Mobile",
        "9876543210"
    )

    email = st.text_input(
        "Email",
        "sample@gmail.com"
    )

    if st.button("Save Changes"):

        st.success(
            "Profile Updated Successfully"
        )

    if st.button("Back Profile"):
        st.session_state.page = "profile"
        st.rerun()


# -----------------------------------
# STUDENT DASHBOARD
# -----------------------------------

def student_dashboard():

    st.title("🎓 Student Dashboard")

    st.metric("Enrolled Courses", 5)

    st.metric("Completed Courses", 2)

    st.metric("Overall Progress", "45%")

    st.info(
        "Welcome Student 👋"
    )


# -----------------------------------
# INSTRUCTOR DASHBOARD
# -----------------------------------

def instructor_dashboard():

    st.title("👨‍🏫 Instructor Dashboard")

    st.metric("Courses Created", 12)

    st.metric("Students Enrolled", 340)

    st.metric("Assignments", 35)

    st.success(
        "Welcome Instructor"
    )


# -----------------------------------
# ADMIN DASHBOARD
# -----------------------------------

def admin_dashboard():

    st.title("🛠 Admin Dashboard")

    st.metric("Total Users", 1500)

    st.metric("Courses", 75)

    st.metric("Instructors", 35)

    st.metric("Students", 1385)

    st.success(
        "Welcome Admin"
    )


# -----------------------------------
# MAIN APP
# -----------------------------------

if "page" not in st.session_state:
    st.session_state.page = "login"

if not st.session_state.logged_in:

    if st.session_state.page == "login":
        login_page()

    elif st.session_state.page == "register":
        registration_page()

    elif st.session_state.page == "forgot":
        forgot_password()

else:

    with st.sidebar:

        st.title("NEXUS LMS")

        st.write(
            f"Welcome {st.session_state.username}"
        )

        menu = st.radio(
            "Navigation",
            [
                "Dashboard",
                "Profile",
                "Edit Profile"
            ]
        )

        if st.button("Logout"):

            st.session_state.logged_in = False
            st.session_state.role = ""
            st.session_state.username = ""

            st.success("Logged Out")

            st.rerun()

    if menu == "Dashboard":

        if st.session_state.role == "Student":
            student_dashboard()

        elif st.session_state.role == "Instructor":
            instructor_dashboard()

        else:
            admin_dashboard()

    elif menu == "Profile":
        profile_page()

    elif menu == "Edit Profile":
        edit_profile()