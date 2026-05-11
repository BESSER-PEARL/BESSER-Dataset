





import java.util.List;
import java.util.ArrayList;

public class camel_organisation_PaaSageCredentials extends Credentials {

    private String password;



    public camel_organisation_PaaSageCredentials(
        String password    ) {
        super(
        );
        this.password = password;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}