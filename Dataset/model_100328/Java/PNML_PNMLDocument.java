





import java.util.List;
import java.util.ArrayList;

public class PNML_PNMLDocument extends LocatedElement {






    private List<NetElement> netelements;




    private URI uri;


    public PNML_PNMLDocument(
    ) {
        super(
        );
        this.netelements = new ArrayList<>();
    }

    public PNML_PNMLDocument(
        ArrayList<NetElement> netelements    ) {
        this.netelements = netelements;
    }


    public List<NetElement> getNetelements() {
        return netelements;
    }

    public void addNetelement(Netelement netelement) {
        this.netelements.add(netelement);
    }
    public URI getUri() {
        return uri;
    }

    public void setUri(URI uri) {
        this.uri = uri;
    }

}