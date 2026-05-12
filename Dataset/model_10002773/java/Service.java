





import java.util.List;
import java.util.ArrayList;

public class Service  {

    private String serviceName;
    private String arrivalDateTime;
    private None type;
    private int serviceId;
    private String departureDateTime;



    public Service(
        String serviceName,        String arrivalDateTime,        None type,        int serviceId,        String departureDateTime    ) {
        this.serviceName = serviceName;
        this.arrivalDateTime = arrivalDateTime;
        this.type = type;
        this.serviceId = serviceId;
        this.departureDateTime = departureDateTime;
    }


    public String getServicename() {
        return serviceName;
    }

    public void setServicename(String serviceName) {
        this.serviceName = serviceName;
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


}