





import java.util.List;
import java.util.ArrayList;

public class data_WebAccount extends MetaInformation {

    private String username;
    private String service;



    public data_WebAccount(
        String username,        String service    ) {
        super(
        );
        this.username = username;
        this.service = service;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getService() {
        return service;
    }

    public void setService(String service) {
        this.service = service;
    }


}