





import java.util.List;
import java.util.ArrayList;

public class Service  {

    private None type;
    private String serviceName;
    private int serviceId;
    private String departureDateTime;
    private String arrivalDateTime;



    public Service(
        None type,        String serviceName,        int serviceId,        String departureDateTime,        String arrivalDateTime    ) {
        this.type = type;
        this.serviceName = serviceName;
        this.serviceId = serviceId;
        this.departureDateTime = departureDateTime;
        this.arrivalDateTime = arrivalDateTime;
    }


    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getServicename() {
        return serviceName;
    }

    public void setServicename(String serviceName) {
        this.serviceName = serviceName;
    }
    public int getServiceid() {
        return serviceId;
    }

    public void setServiceid(int serviceId) {
        this.serviceId = serviceId;
    }
    public String getDeparturedatetime() {
        return departureDateTime;
    }

    public void setDeparturedatetime(String departureDateTime) {
        this.departureDateTime = departureDateTime;
    }
    public String getArrivaldatetime() {
        return arrivalDateTime;
    }

    public void setArrivaldatetime(String arrivalDateTime) {
        this.arrivalDateTime = arrivalDateTime;
    }


}