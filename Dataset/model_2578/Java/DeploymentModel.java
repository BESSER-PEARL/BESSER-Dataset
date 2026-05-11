





import java.util.List;
import java.util.ArrayList;

public class DeploymentModel  {






    private camel_Application camel_application;




    private camel_organisation_User camel_organisation_user;




    private camel_CamelModel camel_camelmodel;


    public DeploymentModel(
    ) {
    }



    public camel_Application getCamel_application() {
        return camel_application;
    }

    public void setCamel_application(camel_Application camel_application) {
        this.camel_application = camel_application;
    }
    public camel_organisation_User getCamel_organisation_user() {
        return camel_organisation_user;
    }

    public void setCamel_organisation_user(camel_organisation_User camel_organisation_user) {
        this.camel_organisation_user = camel_organisation_user;
    }
    public camel_CamelModel getCamel_camelmodel() {
        return camel_camelmodel;
    }

    public void setCamel_camelmodel(camel_CamelModel camel_camelmodel) {
        this.camel_camelmodel = camel_camelmodel;
    }

}