





import java.util.List;
import java.util.ArrayList;

public class application_ApplicationMapper  {

    private String name;
    private String uid;





    private application_ApplicationMappers application_applicationmappers;


    public application_ApplicationMapper(
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

    public application_ApplicationMappers getApplication_applicationmappers() {
        return application_applicationmappers;
    }

    public void setApplication_applicationmappers(application_ApplicationMappers application_applicationmappers) {
        this.application_applicationmappers = application_applicationmappers;
    }

}