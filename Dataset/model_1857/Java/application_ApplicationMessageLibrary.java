





import java.util.List;
import java.util.ArrayList;

public class application_ApplicationMessageLibrary  {

    private String uid;
    private String name;





    private application_ApplicationMessageLibraries application_applicationmessagelibraries;


    public application_ApplicationMessageLibrary(
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

    public application_ApplicationMessageLibraries getApplication_applicationmessagelibraries() {
        return application_applicationmessagelibraries;
    }

    public void setApplication_applicationmessagelibraries(application_ApplicationMessageLibraries application_applicationmessagelibraries) {
        this.application_applicationmessagelibraries = application_applicationmessagelibraries;
    }

}