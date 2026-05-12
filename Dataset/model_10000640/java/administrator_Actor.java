





import java.util.List;
import java.util.ArrayList;

public class administrator_Actor  {






    private search_user_UseCase search_user_usecase;




    private logout_UseCase logout_usecase;




    private login_UseCase login_usecase;




    private create_user_UseCase create_user_usecase;


    public administrator_Actor(
    ) {
    }



    public search_user_UseCase getSearch_user_usecase() {
        return search_user_usecase;
    }

    public void setSearch_user_usecase(search_user_UseCase search_user_usecase) {
        this.search_user_usecase = search_user_usecase;
    }
    public logout_UseCase getLogout_usecase() {
        return logout_usecase;
    }

    public void setLogout_usecase(logout_UseCase logout_usecase) {
        this.logout_usecase = logout_usecase;
    }
    public login_UseCase getLogin_usecase() {
        return login_usecase;
    }

    public void setLogin_usecase(login_UseCase login_usecase) {
        this.login_usecase = login_usecase;
    }
    public create_user_UseCase getCreate_user_usecase() {
        return create_user_usecase;
    }

    public void setCreate_user_usecase(create_user_UseCase create_user_usecase) {
        this.create_user_usecase = create_user_usecase;
    }

}