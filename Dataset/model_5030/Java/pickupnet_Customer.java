





import java.util.List;
import java.util.ArrayList;

public class pickupnet_Customer  {

    private String name;
    private String twitterUserName;
    private String id;



    public pickupnet_Customer(
        String name,        String twitterUserName,        String id    ) {
        this.name = name;
        this.twitterUserName = twitterUserName;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTwitterusername() {
        return twitterUserName;
    }

    public void setTwitterusername(String twitterUserName) {
        this.twitterUserName = twitterUserName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}