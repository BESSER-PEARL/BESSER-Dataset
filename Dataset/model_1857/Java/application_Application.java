





import java.util.List;
import java.util.ArrayList;

public class application_Application  {

    private String uid;
    private String name;





    private application_ApplicationGroup application_applicationgroup;


    public application_Application(
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

    public application_ApplicationGroup getApplication_applicationgroup() {
        return application_applicationgroup;
    }

    public void setApplication_applicationgroup(application_ApplicationGroup application_applicationgroup) {
        this.application_applicationgroup = application_applicationgroup;
    }

}