





import java.util.List;
import java.util.ArrayList;

public class p2_RepositoryType  {

    private String location;





    private p2_LocationType p2_locationtype;


    public p2_RepositoryType(
        String location    ) {
        this.location = location;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public p2_LocationType getP2_locationtype() {
        return p2_locationtype;
    }

    public void setP2_locationtype(p2_LocationType p2_locationtype) {
        this.p2_locationtype = p2_locationtype;
    }

}