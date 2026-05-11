





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_ExternalComponent extends Component {

    private String passwd;
    private String location;
    private String endPoint;
    private String login;
    private String Region;
    private String serviceType;



    public cloudml_core_ExternalComponent(
        String passwd,        String location,        String endPoint,        String login,        String Region,        String serviceType    ) {
        super(
        );
        this.passwd = passwd;
        this.location = location;
        this.endPoint = endPoint;
        this.login = login;
        this.Region = Region;
        this.serviceType = serviceType;
    }


    public String getPasswd() {
        return passwd;
    }

    public void setPasswd(String passwd) {
        this.passwd = passwd;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getEndpoint() {
        return endPoint;
    }

    public void setEndpoint(String endPoint) {
        this.endPoint = endPoint;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public String getRegion() {
        return Region;
    }

    public void setRegion(String Region) {
        this.Region = Region;
    }
    public String getServicetype() {
        return serviceType;
    }

    public void setServicetype(String serviceType) {
        this.serviceType = serviceType;
    }


}