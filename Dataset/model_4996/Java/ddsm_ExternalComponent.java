





import java.util.List;
import java.util.ArrayList;

public class ddsm_ExternalComponent extends Component {

    private String serviceType;
    private String login;
    private String password;
    private String region;
    private String location;





    private ddsm_Provider ddsm_provider;


    public ddsm_ExternalComponent(
        String serviceType,        String login,        String password,        String region,        String location    ) {
        super(
        );
        this.serviceType = serviceType;
        this.login = login;
        this.password = password;
        this.region = region;
        this.location = location;
    }


    public String getServicetype() {
        return serviceType;
    }

    public void setServicetype(String serviceType) {
        this.serviceType = serviceType;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getRegion() {
        return region;
    }

    public void setRegion(String region) {
        this.region = region;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public ddsm_Provider getDdsm_provider() {
        return ddsm_provider;
    }

    public void setDdsm_provider(ddsm_Provider ddsm_provider) {
        this.ddsm_provider = ddsm_provider;
    }

}