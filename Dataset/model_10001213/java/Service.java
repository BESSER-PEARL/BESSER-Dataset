





import java.util.List;
import java.util.ArrayList;

public class Service  {

    private String serviceName;
    private int serviceId;
    private String arrivalDateTime;
    private None type;
    private String departureDateTime;



    public Service(
        String serviceName,        int serviceId,        String arrivalDateTime,        None type,        String departureDateTime    ) {
        this.serviceName = serviceName;
        this.serviceId = serviceId;
        this.arrivalDateTime = arrivalDateTime;
        this.type = type;
        this.departureDateTime = departureDateTime;
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
    public String getArrivaldatetime() {
        return arrivalDateTime;
    }

    public void setArrivaldatetime(String arrivalDateTime) {
        this.arrivalDateTime = arrivalDateTime;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getDeparturedatetime() {
        return departureDateTime;
    }

    public void setDeparturedatetime(String departureDateTime) {
        this.departureDateTime = departureDateTime;
    }


}