





import java.util.List;
import java.util.ArrayList;

public class VALIDATE  {

    private String USERNAME;
    private String PASSWORD;



    public VALIDATE(
        String USERNAME,        String PASSWORD    ) {
        this.USERNAME = USERNAME;
        this.PASSWORD = PASSWORD;
    }


    public String getUsername() {
        return USERNAME;
    }

    public void setUsername(String USERNAME) {
        this.USERNAME = USERNAME;
    }
    public String getPassword() {
        return PASSWORD;
    }

    public void setPassword(String PASSWORD) {
        this.PASSWORD = PASSWORD;
    }


}