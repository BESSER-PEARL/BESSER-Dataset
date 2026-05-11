





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_ExternalComponent extends Component {

    private String serviceType;
    private String Region;
    private String location;
    private String login;
    private String endPoint;
    private String passwd;





    private Provider provider;


    public cloudml_core_ExternalComponent(
        String serviceType,        String Region,        String location,        String login,        String endPoint,        String passwd    ) {
        super(
        );
        this.serviceType = serviceType;
        this.Region = Region;
        this.location = location;
        this.login = login;
        this.endPoint = endPoint;
        this.passwd = passwd;
    }


    public String getServicetype() {
        return serviceType;
    }

    public void setServicetype(String serviceType) {
        this.serviceType = serviceType;
    }
    public String getRegion() {
        return Region;
    }

    public void setRegion(String Region) {
        this.Region = Region;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public String getEndpoint() {
        return endPoint;
    }

    public void setEndpoint(String endPoint) {
        this.endPoint = endPoint;
    }
    public String getPasswd() {
        return passwd;
    }

    public void setPasswd(String passwd) {
        this.passwd = passwd;
    }

    public Provider getProvider() {
        return provider;
    }

    public void setProvider(Provider provider) {
        this.provider = provider;
    }

}