





import java.util.List;
import java.util.ArrayList;

public class ric_LinkGroup  {

    private String title;





    private ric_NavigationRegion ric_navigationregion;




    private List<ric_Link> ric_links;




    private List<ric_LinkGroup> ric_linkgroups;


    public ric_LinkGroup(
        String title    ) {
        this.title = title;
        this.ric_links = new ArrayList<>();
        this.ric_linkgroups = new ArrayList<>();
    }

    public ric_LinkGroup(
        String title        ArrayList<ric_Link> ric_links,        ArrayList<ric_LinkGroup> ric_linkgroups    ) {
        this.title = title;
        this.ric_links = ric_links;
        this.ric_linkgroups = ric_linkgroups;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public ric_NavigationRegion getRic_navigationregion() {
        return ric_navigationregion;
    }

    public void setRic_navigationregion(ric_NavigationRegion ric_navigationregion) {
        this.ric_navigationregion = ric_navigationregion;
    }
    public List<ric_Link> getRic_links() {
        return ric_links;
    }

    public void addRic_link(Ric_link ric_link) {
        this.ric_links.add(ric_link);
    }
    public List<ric_LinkGroup> getRic_linkgroups() {
        return ric_linkgroups;
    }

    public void addRic_linkgroup(Ric_linkgroup ric_linkgroup) {
        this.ric_linkgroups.add(ric_linkgroup);
    }

}