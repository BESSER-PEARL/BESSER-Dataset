





import java.util.List;
import java.util.ArrayList;

public class application_ApplicationRealms  {

    private String name;
    private String uid;





    private application_Application application_application;


    public application_ApplicationRealms(
        String name,        String uid    ) {
        this.name = name;
        this.uid = uid;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public application_Application getApplication_application() {
        return application_application;
    }

    public void setApplication_application(application_Application application_application) {
        this.application_application = application_application;
    }

}