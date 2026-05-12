





import java.util.List;
import java.util.ArrayList;

public class Add_Instructor_UseCase  {






    private Login_UseCase login_usecase;


    public Add_Instructor_UseCase(
    ) {
    }



    public Login_UseCase getLogin_usecase() {
        return login_usecase;
    }

    public void setLogin_usecase(Login_UseCase login_usecase) {
        this.login_usecase = login_usecase;
    }

}