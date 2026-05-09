





import java.util.List;
import java.util.ArrayList;

public class application_ApplicationRecipes  {

    private String uid;
    private String name;





    private application_Application application_application;


    public application_ApplicationRecipes(
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

    public application_Application getApplication_application() {
        return application_application;
    }

    public void setApplication_application(application_Application application_application) {
        this.application_application = application_application;
    }

}