





import java.util.List;
import java.util.ArrayList;

public class cloudml_Provider extends WithProperties {

    private String credentials;



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


}