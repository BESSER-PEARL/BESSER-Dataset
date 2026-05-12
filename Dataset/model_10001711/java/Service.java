





import java.util.List;
import java.util.ArrayList;

public class Service  {

    private int serviceId;
    private String departureDateTime;
    private String serviceName;
    private None type;
    private String arrivalDateTime;



    public Service(
        int serviceId,        String departureDateTime,        String serviceName,        None type,        String arrivalDateTime    ) {
        this.serviceId = serviceId;
        this.departureDateTime = departureDateTime;
        this.serviceName = serviceName;
        this.type = type;
        this.arrivalDateTime = arrivalDateTime;
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
    public String getServicename() {
        return serviceName;
    }

    public void setServicename(String serviceName) {
        this.serviceName = serviceName;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getArrivaldatetime() {
        return arrivalDateTime;
    }

    public void setArrivaldatetime(String arrivalDateTime) {
        this.arrivalDateTime = arrivalDateTime;
    }


}