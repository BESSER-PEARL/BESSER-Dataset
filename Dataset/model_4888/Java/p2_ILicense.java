




import java.util.UUID;

import java.util.List;
import java.util.ArrayList;

public class p2_ILicense  {

    private String body;
    private String location;
    private String UUID;



    public p2_ILicense(
        String body,        String location,        String UUID    ) {
        this.body = body;
        this.location = location;
        this.UUID = UUID;
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
    public String getUuid() {
        return UUID;
    }

    public void setUuid(String UUID) {
        this.UUID = UUID;
    }


}