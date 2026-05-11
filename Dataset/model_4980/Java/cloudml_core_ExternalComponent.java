





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_ExternalComponent extends Component {

    private String Region;
    private String passwd;
    private String endPoint;
    private String serviceType;
    private String location;
    private String login;





    private Provider provider;


    public cloudml_core_ExternalComponent(
        String Region,        String passwd,        String endPoint,        String serviceType,        String location,        String login    ) {
        super(
        );
        this.Region = Region;
        this.passwd = passwd;
        this.endPoint = endPoint;
        this.serviceType = serviceType;
        this.location = location;
        this.login = login;
    }


    public String getRegion() {
        return Region;
    }

    public void setRegion(String Region) {
        this.Region = Region;
    }
    public String getPasswd() {
        return passwd;
    }

    public void setPasswd(String passwd) {
        this.passwd = passwd;
    }
    public String getEndpoint() {
        return endPoint;
    }

    public void setEndpoint(String endPoint) {
        this.endPoint = endPoint;
    }
    public String getServicetype() {
        return serviceType;
    }

    public void setServicetype(String serviceType) {
        this.serviceType = serviceType;
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

    public Provider getProvider() {
        return provider;
    }

    public void setProvider(Provider provider) {
        this.provider = provider;
    }

}