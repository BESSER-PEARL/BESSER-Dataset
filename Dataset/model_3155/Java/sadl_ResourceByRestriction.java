





import java.util.List;
import java.util.ArrayList;

public class sadl_ResourceByRestriction extends ResourceIdentifier {

    private String annType;





    private sadl_ResourceByName sadl_resourcebyname;




    private List<sadl_ContentList> sadl_contentlists;


    public sadl_ResourceByRestriction(
        String annType    ) {
        super(
        );
        this.annType = annType;
        this.sadl_contentlists = new ArrayList<>();
    }

    public sadl_ResourceByRestriction(
        String annType        ArrayList<sadl_ContentList> sadl_contentlists    ) {
        this.annType = annType;
        this.sadl_contentlists = sadl_contentlists;
    }

    public String getAnntype() {
        return annType;
    }

    public void setAnntype(String annType) {
        this.annType = annType;
    }

    public sadl_ResourceByName getSadl_resourcebyname() {
        return sadl_resourcebyname;
    }

    public void setSadl_resourcebyname(sadl_ResourceByName sadl_resourcebyname) {
        this.sadl_resourcebyname = sadl_resourcebyname;
    }
    public List<sadl_ContentList> getSadl_contentlists() {
        return sadl_contentlists;
    }

    public void addSadl_contentlist(Sadl_contentlist sadl_contentlist) {
        this.sadl_contentlists.add(sadl_contentlist);
    }

}