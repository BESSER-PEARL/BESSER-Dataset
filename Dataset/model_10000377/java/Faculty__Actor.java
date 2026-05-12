





import java.util.List;
import java.util.ArrayList;

public class Faculty__Actor  {






    private SignUp_UseCase signup_usecase;




    private Upload_Materials_UseCase upload_materials_usecase;




    private Logout_UseCase logout_usecase;




    private Login_UseCase login_usecase;




    private View___Modify_the_Uploaded_Materials_UseCase view___modify_the_uploaded_materials_usecase;




    private View_Questions_And_Post_Answers_UseCase view_questions_and_post_answers_usecase;


    public Faculty__Actor(
    ) {
    }



    public SignUp_UseCase getSignup_usecase() {
        return signup_usecase;
    }

    public void setSignup_usecase(SignUp_UseCase signup_usecase) {
        this.signup_usecase = signup_usecase;
    }
    public Upload_Materials_UseCase getUpload_materials_usecase() {
        return upload_materials_usecase;
    }

    public void setUpload_materials_usecase(Upload_Materials_UseCase upload_materials_usecase) {
        this.upload_materials_usecase = upload_materials_usecase;
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
    public View___Modify_the_Uploaded_Materials_UseCase getView___modify_the_uploaded_materials_usecase() {
        return view___modify_the_uploaded_materials_usecase;
    }

    public void setView___modify_the_uploaded_materials_usecase(View___Modify_the_Uploaded_Materials_UseCase view___modify_the_uploaded_materials_usecase) {
        this.view___modify_the_uploaded_materials_usecase = view___modify_the_uploaded_materials_usecase;
    }
    public View_Questions_And_Post_Answers_UseCase getView_questions_and_post_answers_usecase() {
        return view_questions_and_post_answers_usecase;
    }

    public void setView_questions_and_post_answers_usecase(View_Questions_And_Post_Answers_UseCase view_questions_and_post_answers_usecase) {
        this.view_questions_and_post_answers_usecase = view_questions_and_post_answers_usecase;
    }

}