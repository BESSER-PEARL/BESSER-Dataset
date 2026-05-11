





import java.util.List;
import java.util.ArrayList;

public class iso20022_SemanticMarkup extends ModelEntity {

    private String type;





    private iso20022_RepositoryConcept iso20022_repositoryconcept;




    private List<iso20022_SemanticMarkupElement> iso20022_semanticmarkupelements;


    public iso20022_SemanticMarkup(
        String type    ) {
        super(
        );
        this.type = type;
        this.iso20022_semanticmarkupelements = new ArrayList<>();
    }

    public iso20022_SemanticMarkup(
        String type        ArrayList<iso20022_SemanticMarkupElement> iso20022_semanticmarkupelements    ) {
        this.type = type;
        this.iso20022_semanticmarkupelements = iso20022_semanticmarkupelements;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public iso20022_RepositoryConcept getIso20022_repositoryconcept() {
        return iso20022_repositoryconcept;
    }

    public void setIso20022_repositoryconcept(iso20022_RepositoryConcept iso20022_repositoryconcept) {
        this.iso20022_repositoryconcept = iso20022_repositoryconcept;
    }
    public List<iso20022_SemanticMarkupElement> getIso20022_semanticmarkupelements() {
        return iso20022_semanticmarkupelements;
    }

    public void addIso20022_semanticmarkupelement(Iso20022_semanticmarkupelement iso20022_semanticmarkupelement) {
        this.iso20022_semanticmarkupelements.add(iso20022_semanticmarkupelement);
    }

}