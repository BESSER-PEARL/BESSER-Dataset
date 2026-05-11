





import java.util.List;
import java.util.ArrayList;

public class owl_OWLDataRange extends RDFSClass {






    private List<owl_RDFSLiteral> owl_rdfsliterals;


    public owl_OWLDataRange(
    ) {
        super(
        );
        this.owl_rdfsliterals = new ArrayList<>();
    }

    public owl_OWLDataRange(
        ArrayList<owl_RDFSLiteral> owl_rdfsliterals    ) {
        this.owl_rdfsliterals = owl_rdfsliterals;
    }


    public List<owl_RDFSLiteral> getOwl_rdfsliterals() {
        return owl_rdfsliterals;
    }

    public void addOwl_rdfsliteral(Owl_rdfsliteral owl_rdfsliteral) {
        this.owl_rdfsliterals.add(owl_rdfsliteral);
    }

}