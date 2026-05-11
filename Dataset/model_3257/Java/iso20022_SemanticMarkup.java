





import java.util.List;
import java.util.ArrayList;

public class iso20022_SemanticMarkup extends ModelEntity {

    private String type;





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

    public List<iso20022_SemanticMarkupElement> getIso20022_semanticmarkupelements() {
        return iso20022_semanticmarkupelements;
    }

    public void addIso20022_semanticmarkupelement(Iso20022_semanticmarkupelement iso20022_semanticmarkupelement) {
        this.iso20022_semanticmarkupelements.add(iso20022_semanticmarkupelement);
    }

}