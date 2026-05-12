





import java.util.List;
import java.util.ArrayList;

public class rdal_SubElementReference extends IdentifiedElement {

    private String weight;
    private String referencedElementEntries;





    private rdal_ElementRefinement rdal_elementrefinement;


    public rdal_SubElementReference(
        String weight,        String referencedElementEntries    ) {
        super(
        );
        this.weight = weight;
        this.referencedElementEntries = referencedElementEntries;
    }


    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getReferencedelemententries() {
        return referencedElementEntries;
    }

    public void setReferencedelemententries(String referencedElementEntries) {
        this.referencedElementEntries = referencedElementEntries;
    }

    public rdal_ElementRefinement getRdal_elementrefinement() {
        return rdal_elementrefinement;
    }

    public void setRdal_elementrefinement(rdal_ElementRefinement rdal_elementrefinement) {
        this.rdal_elementrefinement = rdal_elementrefinement;
    }

}