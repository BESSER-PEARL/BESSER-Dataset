





import java.util.List;
import java.util.ArrayList;

public class org.k1s.nppn_PetriNet extends HasName, HasLabel {

    private String kind;
    private String timeType;





    private List<nppn_Page> nppn_pages;


    public org.k1s.nppn_PetriNet(
        String kind,        String timeType    ) {
        super(
        );
        this.kind = kind;
        this.timeType = timeType;
        this.nppn_pages = new ArrayList<>();
    }

    public org.k1s.nppn_PetriNet(
        String kind,        String timeType        ArrayList<nppn_Page> nppn_pages    ) {
        this.kind = kind;
        this.timeType = timeType;
        this.nppn_pages = nppn_pages;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getTimetype() {
        return timeType;
    }

    public void setTimetype(String timeType) {
        this.timeType = timeType;
    }

    public List<nppn_Page> getNppn_pages() {
        return nppn_pages;
    }

    public void addNppn_page(Nppn_page nppn_page) {
        this.nppn_pages.add(nppn_page);
    }

}