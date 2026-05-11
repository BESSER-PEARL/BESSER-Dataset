





import java.util.List;
import java.util.ArrayList;

public class ric_NavigationRegion  {

    private String orientation;





    private List<ric_LinkGroup> ric_linkgroups;




    private ric_Portal ric_portal;




    private ric_HeaderRegion ric_headerregion;


    public ric_NavigationRegion(
        String orientation    ) {
        this.orientation = orientation;
        this.ric_linkgroups = new ArrayList<>();
    }

    public ric_NavigationRegion(
        String orientation        ArrayList<ric_LinkGroup> ric_linkgroups    ) {
        this.orientation = orientation;
        this.ric_linkgroups = ric_linkgroups;
    }

    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }

    public List<ric_LinkGroup> getRic_linkgroups() {
        return ric_linkgroups;
    }

    public void addRic_linkgroup(Ric_linkgroup ric_linkgroup) {
        this.ric_linkgroups.add(ric_linkgroup);
    }
    public ric_Portal getRic_portal() {
        return ric_portal;
    }

    public void setRic_portal(ric_Portal ric_portal) {
        this.ric_portal = ric_portal;
    }
    public ric_HeaderRegion getRic_headerregion() {
        return ric_headerregion;
    }

    public void setRic_headerregion(ric_HeaderRegion ric_headerregion) {
        this.ric_headerregion = ric_headerregion;
    }

}