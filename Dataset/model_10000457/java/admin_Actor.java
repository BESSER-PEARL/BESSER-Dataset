





import java.util.List;
import java.util.ArrayList;

public class admin_Actor  {






    private login_external login_external;




    private modify_list_of_students_external modify_list_of_students_external;




    private logout_external logout_external;


    public admin_Actor(
    ) {
    }



    public login_external getLogin_external() {
        return login_external;
    }

    public void setLogin_external(login_external login_external) {
        this.login_external = login_external;
    }
    public modify_list_of_students_external getModify_list_of_students_external() {
        return modify_list_of_students_external;
    }

    public void setModify_list_of_students_external(modify_list_of_students_external modify_list_of_students_external) {
        this.modify_list_of_students_external = modify_list_of_students_external;
    }
    public logout_external getLogout_external() {
        return logout_external;
    }

    public void setLogout_external(logout_external logout_external) {
        this.logout_external = logout_external;
    }

}