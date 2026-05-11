





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Provider extends CloudMLElementWithProperties {

    private String credentials;



    public cloudml_core_Provider(
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


}