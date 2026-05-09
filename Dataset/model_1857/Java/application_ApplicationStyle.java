





import java.util.List;
import java.util.ArrayList;

public class application_ApplicationStyle  {

    private String uid;
    private String name;





    private application_ApplicationStyleLibraries application_applicationstylelibraries;


    public application_ApplicationStyle(
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

    public application_ApplicationStyleLibraries getApplication_applicationstylelibraries() {
        return application_applicationstylelibraries;
    }

    public void setApplication_applicationstylelibraries(application_ApplicationStyleLibraries application_applicationstylelibraries) {
        this.application_applicationstylelibraries = application_applicationstylelibraries;
    }

}