





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_ILicense  {

    private String location;
    private String digest;
    private String body;



    public aggregator_p2_ILicense(
        String location,        String digest,        String body    ) {
        this.location = location;
        this.digest = digest;
        this.body = body;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
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


}