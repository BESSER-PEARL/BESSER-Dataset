





import java.util.List;
import java.util.ArrayList;

public class model_StringToService  {

    private String key;





    private model_Application model_application;




    private model_Service model_service;


    public model_StringToService(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public model_Application getModel_application() {
        return model_application;
    }

    public void setModel_application(model_Application model_application) {
        this.model_application = model_application;
    }
    public model_Service getModel_service() {
        return model_service;
    }

    public void setModel_service(model_Service model_service) {
        this.model_service = model_service;
    }

}