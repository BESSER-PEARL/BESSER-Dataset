





import java.util.List;
import java.util.ArrayList;

public class data_WebAccount extends MetaInformation {

    private String username;



    public data_WebAccount(
        String username    ) {
        super(
        );
        this.username = username;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }


}