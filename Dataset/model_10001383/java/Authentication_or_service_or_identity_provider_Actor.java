





import java.util.List;
import java.util.ArrayList;

public class Authentication_or_service_or_identity_provider_Actor  {






    private Log_in__sign_in_page_UseCase log_in__sign_in_page_usecase;




    private user_authentication_cookie_UseCase user_authentication_cookie_usecase;


    public Authentication_or_service_or_identity_provider_Actor(
    ) {
    }



    public Log_in__sign_in_page_UseCase getLog_in__sign_in_page_usecase() {
        return log_in__sign_in_page_usecase;
    }

    public void setLog_in__sign_in_page_usecase(Log_in__sign_in_page_UseCase log_in__sign_in_page_usecase) {
        this.log_in__sign_in_page_usecase = log_in__sign_in_page_usecase;
    }
    public user_authentication_cookie_UseCase getUser_authentication_cookie_usecase() {
        return user_authentication_cookie_usecase;
    }

    public void setUser_authentication_cookie_usecase(user_authentication_cookie_UseCase user_authentication_cookie_usecase) {
        this.user_authentication_cookie_usecase = user_authentication_cookie_usecase;
    }

}