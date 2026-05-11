





import java.util.List;
import java.util.ArrayList;

public class p2_UnitType  {

    private String id;
    private String state;
    private String version;





    private p2_LocationType p2_locationtype;


    public p2_UnitType(
        String id,        String state,        String version    ) {
        this.id = id;
        this.state = state;
        this.version = version;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public p2_LocationType getP2_locationtype() {
        return p2_locationtype;
    }

    public void setP2_locationtype(p2_LocationType p2_locationtype) {
        this.p2_locationtype = p2_locationtype;
    }

}