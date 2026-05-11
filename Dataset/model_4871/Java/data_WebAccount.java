





import java.util.List;
import java.util.ArrayList;

public class data_WebAccount extends MetaInformation {

    private String service;
    private String username;



    public data_WebAccount(
        String service,        String username    ) {
        super(
        );
        this.service = service;
        this.username = username;
    }


    public String getService() {
        return service;
    }

    public void setService(String service) {
        this.service = service;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }


}