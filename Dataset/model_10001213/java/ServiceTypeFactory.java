





import java.util.List;
import java.util.ArrayList;

public class ServiceTypeFactory  {

    private String type;
    private None getServiceType;





    private Service service;


    public ServiceTypeFactory(
        String type,        None getServiceType    ) {
        this.type = type;
        this.getServiceType = getServiceType;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public None getGetservicetype() {
        return getServiceType;
    }

    public void setGetservicetype(None getServiceType) {
        this.getServiceType = getServiceType;
    }

    public Service getService() {
        return service;
    }

    public void setService(Service service) {
        this.service = service;
    }

}