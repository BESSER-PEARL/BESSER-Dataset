





import java.util.List;
import java.util.ArrayList;

public class cloudml_ExternalComponent extends Component {

    private String endPoint;
    private String Region;
    private String serviceType;
    private String location;
    private String login;
    private String passwd;





    private cloudml_Provider cloudml_provider;




    private cloudml_CloudMLModel cloudml_cloudmlmodel;




    private List<cloudml_VMPort> cloudml_vmports;


    public cloudml_ExternalComponent(
        String endPoint,        String Region,        String serviceType,        String location,        String login,        String passwd    ) {
        super(
        );
        this.endPoint = endPoint;
        this.Region = Region;
        this.serviceType = serviceType;
        this.location = location;
        this.login = login;
        this.passwd = passwd;
        this.cloudml_vmports = new ArrayList<>();
    }

    public cloudml_ExternalComponent(
        String endPoint,        String Region,        String serviceType,        String location,        String login,        String passwd        ArrayList<cloudml_VMPort> cloudml_vmports    ) {
        this.endPoint = endPoint;
        this.Region = Region;
        this.serviceType = serviceType;
        this.location = location;
        this.login = login;
        this.passwd = passwd;
        this.cloudml_vmports = cloudml_vmports;
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
    public String getPasswd() {
        return passwd;
    }

    public void setPasswd(String passwd) {
        this.passwd = passwd;
    }

    public cloudml_Provider getCloudml_provider() {
        return cloudml_provider;
    }

    public void setCloudml_provider(cloudml_Provider cloudml_provider) {
        this.cloudml_provider = cloudml_provider;
    }
    public cloudml_CloudMLModel getCloudml_cloudmlmodel() {
        return cloudml_cloudmlmodel;
    }

    public void setCloudml_cloudmlmodel(cloudml_CloudMLModel cloudml_cloudmlmodel) {
        this.cloudml_cloudmlmodel = cloudml_cloudmlmodel;
    }
    public List<cloudml_VMPort> getCloudml_vmports() {
        return cloudml_vmports;
    }

    public void addCloudml_vmport(Cloudml_vmport cloudml_vmport) {
        this.cloudml_vmports.add(cloudml_vmport);
    }

}