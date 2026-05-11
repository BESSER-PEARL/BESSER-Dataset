





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_ILicense  {

    private String digest;
    private String location;
    private String body;



    public aggregator_p2_ILicense(
        String digest,        String location,        String body    ) {
        this.digest = digest;
        this.location = location;
        this.body = body;
    }


    public String getDigest() {
        return digest;
    }

    public void setDigest(String digest) {
        this.digest = digest;
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