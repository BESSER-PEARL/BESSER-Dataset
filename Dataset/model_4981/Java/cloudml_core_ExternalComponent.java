





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_ExternalComponent extends Component {

    private String login;
    private String endPoint;
    private String Region;
    private String passwd;
    private String location;
    private String serviceType;





    private Provider provider;


    public cloudml_core_ExternalComponent(
        String login,        String endPoint,        String Region,        String passwd,        String location,        String serviceType    ) {
        super(
        );
        this.login = login;
        this.endPoint = endPoint;
        this.Region = Region;
        this.passwd = passwd;
        this.location = location;
        this.serviceType = serviceType;
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
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getServicetype() {
        return serviceType;
    }

    public void setServicetype(String serviceType) {
        this.serviceType = serviceType;
    }

    public Provider getProvider() {
        return provider;
    }

    public void setProvider(Provider provider) {
        this.provider = provider;
    }

}