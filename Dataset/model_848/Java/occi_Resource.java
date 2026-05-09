





import java.util.List;
import java.util.ArrayList;

public class occi_Resource extends Entity {

    private String summary;





    private List<occi_Link> occi_links;




    private occi_Link occi_link;




    private occi_Link occi_link;




    private List<occi_Link> occi_links;


    public occi_Resource(
        String summary    ) {
        super(
        );
        this.summary = summary;
        this.occi_links = new ArrayList<>();
        this.occi_links = new ArrayList<>();
    }

    public occi_Resource(
        String summary        ArrayList<occi_Link> occi_links,        ArrayList<occi_Link> occi_links    ) {
        this.summary = summary;
        this.occi_links = occi_links;
        this.occi_links = occi_links;
    }

    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }

    public List<occi_Link> getOcci_links() {
        return occi_links;
    }

    public void addOcci_link(Occi_link occi_link) {
        this.occi_links.add(occi_link);
    }
    public occi_Link getOcci_link() {
        return occi_link;
    }

    public void setOcci_link(occi_Link occi_link) {
        this.occi_link = occi_link;
    }
    public occi_Link getOcci_link() {
        return occi_link;
    }

    public void setOcci_link(occi_Link occi_link) {
        this.occi_link = occi_link;
    }
    public List<occi_Link> getOcci_links() {
        return occi_links;
    }

    public void addOcci_link(Occi_link occi_link) {
        this.occi_links.add(occi_link);
    }

}