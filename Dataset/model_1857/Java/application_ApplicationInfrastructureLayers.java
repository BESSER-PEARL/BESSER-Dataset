





import java.util.List;
import java.util.ArrayList;

public class application_ApplicationInfrastructureLayers  {

    private String name;
    private String uid;





    private application_Application application_application;




    private List<application_ApplicationInfrastructureLayer> application_applicationinfrastructurelayers;


    public application_ApplicationInfrastructureLayers(
        String name,        String uid    ) {
        this.name = name;
        this.uid = uid;
        this.application_applicationinfrastructurelayers = new ArrayList<>();
    }

    public application_ApplicationInfrastructureLayers(
        String name,        String uid        ArrayList<application_ApplicationInfrastructureLayer> application_applicationinfrastructurelayers    ) {
        this.name = name;
        this.uid = uid;
        this.application_applicationinfrastructurelayers = application_applicationinfrastructurelayers;
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
    public List<application_ApplicationInfrastructureLayer> getApplication_applicationinfrastructurelayers() {
        return application_applicationinfrastructurelayers;
    }

    public void addApplication_applicationinfrastructurelayer(Application_applicationinfrastructurelayer application_applicationinfrastructurelayer) {
        this.application_applicationinfrastructurelayers.add(application_applicationinfrastructurelayer);
    }

}