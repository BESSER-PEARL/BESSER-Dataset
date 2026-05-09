





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_SGMLCatalog extends NamedElement {






    private List<mancoosimm_SGMLDocument> mancoosimm_sgmldocuments;


    public mancoosimm_SGMLCatalog(
    ) {
        super(
        );
        this.mancoosimm_sgmldocuments = new ArrayList<>();
    }

    public mancoosimm_SGMLCatalog(
        ArrayList<mancoosimm_SGMLDocument> mancoosimm_sgmldocuments    ) {
        this.mancoosimm_sgmldocuments = mancoosimm_sgmldocuments;
    }


    public List<mancoosimm_SGMLDocument> getMancoosimm_sgmldocuments() {
        return mancoosimm_sgmldocuments;
    }

    public void addMancoosimm_sgmldocument(Mancoosimm_sgmldocument mancoosimm_sgmldocument) {
        this.mancoosimm_sgmldocuments.add(mancoosimm_sgmldocument);
    }

}