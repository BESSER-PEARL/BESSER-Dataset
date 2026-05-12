





import java.util.List;
import java.util.ArrayList;

public class Student_Actor  {






    private check_details_UseCase check_details_usecase;




    private Name_UseCase name_usecase;




    private Login_UseCase1 login_usecase1;




    private registered_UseCase registered_usecase;


    public Student_Actor(
    ) {
    }



    public check_details_UseCase getCheck_details_usecase() {
        return check_details_usecase;
    }

    public void setCheck_details_usecase(check_details_UseCase check_details_usecase) {
        this.check_details_usecase = check_details_usecase;
    }
    public Name_UseCase getName_usecase() {
        return name_usecase;
    }

    public void setName_usecase(Name_UseCase name_usecase) {
        this.name_usecase = name_usecase;
    }
    public Login_UseCase1 getLogin_usecase1() {
        return login_usecase1;
    }

    public void setLogin_usecase1(Login_UseCase1 login_usecase1) {
        this.login_usecase1 = login_usecase1;
    }
    public registered_UseCase getRegistered_usecase() {
        return registered_usecase;
    }

    public void setRegistered_usecase(registered_UseCase registered_usecase) {
        this.registered_usecase = registered_usecase;
    }

}