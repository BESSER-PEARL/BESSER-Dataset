





import java.util.List;
import java.util.ArrayList;

public class ric_LinkGroup  {

    private String title;





    private List<ric_LinkGroup> ric_linkgroups;




    private List<ric_Link> ric_links;


    public ric_LinkGroup(
        String title    ) {
        this.title = title;
        this.ric_linkgroups = new ArrayList<>();
        this.ric_links = new ArrayList<>();
    }

    public ric_LinkGroup(
        String title        ArrayList<ric_LinkGroup> ric_linkgroups,        ArrayList<ric_Link> ric_links    ) {
        this.title = title;
        this.ric_linkgroups = ric_linkgroups;
        this.ric_links = ric_links;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<ric_LinkGroup> getRic_linkgroups() {
        return ric_linkgroups;
    }

    public void addRic_linkgroup(Ric_linkgroup ric_linkgroup) {
        this.ric_linkgroups.add(ric_linkgroup);
    }
    public List<ric_Link> getRic_links() {
        return ric_links;
    }

    public void addRic_link(Ric_link ric_link) {
        this.ric_links.add(ric_link);
    }

}