





import java.util.List;
import java.util.ArrayList;

public class ServiceTypeFactory  {

    private None getServiceType;
    private String type;





    private Service service;


    public ServiceTypeFactory(
        None getServiceType,        String type    ) {
        this.getServiceType = getServiceType;
        this.type = type;
    }


    public None getGetservicetype() {
        return getServiceType;
    }

    public void setGetservicetype(None getServiceType) {
        this.getServiceType = getServiceType;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Service getService() {
        return service;
    }

    public void setService(Service service) {
        this.service = service;
    }

}