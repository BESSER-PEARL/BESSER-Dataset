





import java.util.List;
import java.util.ArrayList;

public class WebApp_Twitter extends ExternalSource {

    private String username;



    public WebApp_Twitter(
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