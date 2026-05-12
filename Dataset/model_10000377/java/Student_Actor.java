





import java.util.List;
import java.util.ArrayList;

public class Student_Actor  {






    private Logout_UseCase logout_usecase;




    private Login_UseCase login_usecase;




    private SignUp_UseCase signup_usecase;




    private Post_Questions_UseCase post_questions_usecase;




    private View_The_Uploaded_Materials_UseCase view_the_uploaded_materials_usecase;


    public Student_Actor(
    ) {
    }



    public Logout_UseCase getLogout_usecase() {
        return logout_usecase;
    }

    public void setLogout_usecase(Logout_UseCase logout_usecase) {
        this.logout_usecase = logout_usecase;
    }
    public Login_UseCase getLogin_usecase() {
        return login_usecase;
    }

    public void setLogin_usecase(Login_UseCase login_usecase) {
        this.login_usecase = login_usecase;
    }
    public SignUp_UseCase getSignup_usecase() {
        return signup_usecase;
    }

    public void setSignup_usecase(SignUp_UseCase signup_usecase) {
        this.signup_usecase = signup_usecase;
    }
    public Post_Questions_UseCase getPost_questions_usecase() {
        return post_questions_usecase;
    }

    public void setPost_questions_usecase(Post_Questions_UseCase post_questions_usecase) {
        this.post_questions_usecase = post_questions_usecase;
    }
    public View_The_Uploaded_Materials_UseCase getView_the_uploaded_materials_usecase() {
        return view_the_uploaded_materials_usecase;
    }

    public void setView_the_uploaded_materials_usecase(View_The_Uploaded_Materials_UseCase view_the_uploaded_materials_usecase) {
        this.view_the_uploaded_materials_usecase = view_the_uploaded_materials_usecase;
    }

}