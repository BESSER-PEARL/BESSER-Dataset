





import java.util.List;
import java.util.ArrayList;

public class cloudml_Provider extends CloudMLElementWithProperties {

    private String credentials;





    private cloudml_CloudMLModel cloudml_cloudmlmodel;


    public cloudml_Provider(
        String credentials    ) {
        super(
        );
        this.credentials = credentials;
    }


    public String getCredentials() {
        return credentials;
    }

    public void setCredentials(String credentials) {
        this.credentials = credentials;
    }

    public cloudml_CloudMLModel getCloudml_cloudmlmodel() {
        return cloudml_cloudmlmodel;
    }

    public void setCloudml_cloudmlmodel(cloudml_CloudMLModel cloudml_cloudmlmodel) {
        this.cloudml_cloudmlmodel = cloudml_cloudmlmodel;
    }

}