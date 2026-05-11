





import java.util.List;
import java.util.ArrayList;

public class sadl_ResourceBySetOp extends ResourceIdentifier {

    private String op;
    private String annType;





    private List<sadl_ContentList> sadl_contentlists;


    public sadl_ResourceBySetOp(
        String op,        String annType    ) {
        super(
        );
        this.op = op;
        this.annType = annType;
        this.sadl_contentlists = new ArrayList<>();
    }

    public sadl_ResourceBySetOp(
        String op,        String annType        ArrayList<sadl_ContentList> sadl_contentlists    ) {
        this.op = op;
        this.annType = annType;
        this.sadl_contentlists = sadl_contentlists;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }
    public String getAnntype() {
        return annType;
    }

    public void setAnntype(String annType) {
        this.annType = annType;
    }

    public List<sadl_ContentList> getSadl_contentlists() {
        return sadl_contentlists;
    }

    public void addSadl_contentlist(Sadl_contentlist sadl_contentlist) {
        this.sadl_contentlists.add(sadl_contentlist);
    }

}