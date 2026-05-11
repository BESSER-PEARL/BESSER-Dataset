





import java.util.List;
import java.util.ArrayList;

public class sadl_ResourceName  {

    private String annType;
    private String name;





    private List<sadl_ContentList> sadl_contentlists;


    public sadl_ResourceName(
        String annType,        String name    ) {
        this.annType = annType;
        this.name = name;
        this.sadl_contentlists = new ArrayList<>();
    }

    public sadl_ResourceName(
        String annType,        String name        ArrayList<sadl_ContentList> sadl_contentlists    ) {
        this.annType = annType;
        this.name = name;
        this.sadl_contentlists = sadl_contentlists;
    }

    public String getAnntype() {
        return annType;
    }

    public void setAnntype(String annType) {
        this.annType = annType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<sadl_ContentList> getSadl_contentlists() {
        return sadl_contentlists;
    }

    public void addSadl_contentlist(Sadl_contentlist sadl_contentlist) {
        this.sadl_contentlists.add(sadl_contentlist);
    }

}