





import java.util.List;
import java.util.ArrayList;

public class login_or_sign_in_page_UseCase  {






    private Authentication_Service_or_identity_provider_Actor authentication_service_or_identity_provider_actor;


    public login_or_sign_in_page_UseCase(
    ) {
    }



    public Authentication_Service_or_identity_provider_Actor getAuthentication_service_or_identity_provider_actor() {
        return authentication_service_or_identity_provider_actor;
    }

    public void setAuthentication_service_or_identity_provider_actor(Authentication_Service_or_identity_provider_Actor authentication_service_or_identity_provider_actor) {
        this.authentication_service_or_identity_provider_actor = authentication_service_or_identity_provider_actor;
    }

}