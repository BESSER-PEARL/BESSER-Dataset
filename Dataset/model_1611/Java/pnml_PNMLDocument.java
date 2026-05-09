





import java.util.List;
import java.util.ArrayList;

public class pnml_PNMLDocument  {

    private String location;





    private List<pnml_NetElement> pnml_netelements;


    public pnml_PNMLDocument(
        String location    ) {
        this.location = location;
        this.pnml_netelements = new ArrayList<>();
    }

    public pnml_PNMLDocument(
        String location        ArrayList<pnml_NetElement> pnml_netelements    ) {
        this.location = location;
        this.pnml_netelements = pnml_netelements;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public List<pnml_NetElement> getPnml_netelements() {
        return pnml_netelements;
    }

    public void addPnml_netelement(Pnml_netelement pnml_netelement) {
        this.pnml_netelements.add(pnml_netelement);
    }

}