





import java.util.List;
import java.util.ArrayList;

public class application_ApplicationUIPackage  {

    private String uid;
    private String name;





    private application_ApplicationUILayer application_applicationuilayer;


    public application_ApplicationUIPackage(
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

    public application_ApplicationUILayer getApplication_applicationuilayer() {
        return application_applicationuilayer;
    }

    public void setApplication_applicationuilayer(application_ApplicationUILayer application_applicationuilayer) {
        this.application_applicationuilayer = application_applicationuilayer;
    }

}