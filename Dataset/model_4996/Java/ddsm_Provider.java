





import java.util.List;
import java.util.ArrayList;

public class ddsm_Provider extends CloudElement {

    private String credentialsPath;
    private String type;



    public ddsm_Provider(
        String credentialsPath,        String type    ) {
        super(
        );
        this.credentialsPath = credentialsPath;
        this.type = type;
    }


    public String getCredentialspath() {
        return credentialsPath;
    }

    public void setCredentialspath(String credentialsPath) {
        this.credentialsPath = credentialsPath;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}