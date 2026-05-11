





import java.util.List;
import java.util.ArrayList;

public class cloudml_ExternalComponent extends Component {

    private String login;
    private String serviceType;
    private String Region;
    private String endPoint;
    private String passwd;
    private String location;





    private cloudml_CloudMLModel cloudml_cloudmlmodel;




    private List<cloudml_VMPort> cloudml_vmports;




    private cloudml_Provider cloudml_provider;


    public cloudml_ExternalComponent(
        String login,        String serviceType,        String Region,        String endPoint,        String passwd,        String location    ) {
        super(
        );
        this.login = login;
        this.serviceType = serviceType;
        this.Region = Region;
        this.endPoint = endPoint;
        this.passwd = passwd;
        this.location = location;
        this.cloudml_vmports = new ArrayList<>();
    }

    public cloudml_ExternalComponent(
        String login,        String serviceType,        String Region,        String endPoint,        String passwd,        String location        ArrayList<cloudml_VMPort> cloudml_vmports    ) {
        this.login = login;
        this.serviceType = serviceType;
        this.Region = Region;
        this.endPoint = endPoint;
        this.passwd = passwd;
        this.location = location;
        this.cloudml_vmports = cloudml_vmports;
    }

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
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
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
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
    public cloudml_Provider getCloudml_provider() {
        return cloudml_provider;
    }

    public void setCloudml_provider(cloudml_Provider cloudml_provider) {
        this.cloudml_provider = cloudml_provider;
    }

}