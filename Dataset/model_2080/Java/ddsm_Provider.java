





import java.util.List;
import java.util.ArrayList;

public class ddsm_Provider extends CloudElement {

    private String type;
    private String credentialsPath;



    public ddsm_Provider(
        String type,        String credentialsPath    ) {
        super(
        );
        this.type = type;
        this.credentialsPath = credentialsPath;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getCredentialspath() {
        return credentialsPath;
    }

    public void setCredentialspath(String credentialsPath) {
        this.credentialsPath = credentialsPath;
    }


}