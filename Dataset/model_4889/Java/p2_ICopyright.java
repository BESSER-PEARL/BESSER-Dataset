





import java.util.List;
import java.util.ArrayList;

public class p2_ICopyright  {

    private String body;
    private String location;





    private p2_IInstallableUnit p2_iinstallableunit;


    public p2_ICopyright(
        String body,        String location    ) {
        this.body = body;
        this.location = location;
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

    public p2_IInstallableUnit getP2_iinstallableunit() {
        return p2_iinstallableunit;
    }

    public void setP2_iinstallableunit(p2_IInstallableUnit p2_iinstallableunit) {
        this.p2_iinstallableunit = p2_iinstallableunit;
    }

}