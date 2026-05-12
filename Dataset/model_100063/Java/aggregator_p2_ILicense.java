





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_ILicense  {

    private String digest;
    private String body;
    private String location;



    public aggregator_p2_ILicense(
        String digest,        String body,        String location    ) {
        this.digest = digest;
        this.body = body;
        this.location = location;
    }


    public String getDigest() {
        return digest;
    }

    public void setDigest(String digest) {
        this.digest = digest;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}