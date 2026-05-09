





import java.util.List;
import java.util.ArrayList;

public class application_ApplicationRealm  {

    private String uid;
    private String name;





    private application_ApplicationRealms application_applicationrealms;




    private application_Roles application_roles;


    public application_ApplicationRealm(
        String uid,        String name    ) {
        this.uid = uid;
        this.name = name;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public application_ApplicationRealms getApplication_applicationrealms() {
        return application_applicationrealms;
    }

    public void setApplication_applicationrealms(application_ApplicationRealms application_applicationrealms) {
        this.application_applicationrealms = application_applicationrealms;
    }
    public application_Roles getApplication_roles() {
        return application_roles;
    }

    public void setApplication_roles(application_Roles application_roles) {
        this.application_roles = application_roles;
    }

}