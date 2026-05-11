





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_ICopyright  {

    private String location;
    private String body;



    public aggregator_p2_ICopyright(
        String location,        String body    ) {
        this.location = location;
        this.body = body;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }


}