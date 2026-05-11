





import java.util.List;
import java.util.ArrayList;

public class owl_DatatypeSlot  {






    private owl_Individual owl_individual;




    private owl_Individual owl_individual;




    private List<owl_RDFSLiteral> owl_rdfsliterals;




    private owl_OWLDatatypeProperty owl_owldatatypeproperty;


    public owl_DatatypeSlot(
    ) {
        this.owl_rdfsliterals = new ArrayList<>();
    }

    public owl_DatatypeSlot(
        ArrayList<owl_RDFSLiteral> owl_rdfsliterals    ) {
        this.owl_rdfsliterals = owl_rdfsliterals;
    }


    public owl_Individual getOwl_individual() {
        return owl_individual;
    }

    public void setOwl_individual(owl_Individual owl_individual) {
        this.owl_individual = owl_individual;
    }
    public owl_Individual getOwl_individual() {
        return owl_individual;
    }

    public void setOwl_individual(owl_Individual owl_individual) {
        this.owl_individual = owl_individual;
    }
    public List<owl_RDFSLiteral> getOwl_rdfsliterals() {
        return owl_rdfsliterals;
    }

    public void addOwl_rdfsliteral(Owl_rdfsliteral owl_rdfsliteral) {
        this.owl_rdfsliterals.add(owl_rdfsliteral);
    }
    public owl_OWLDatatypeProperty getOwl_owldatatypeproperty() {
        return owl_owldatatypeproperty;
    }

    public void setOwl_owldatatypeproperty(owl_OWLDatatypeProperty owl_owldatatypeproperty) {
        this.owl_owldatatypeproperty = owl_owldatatypeproperty;
    }

}