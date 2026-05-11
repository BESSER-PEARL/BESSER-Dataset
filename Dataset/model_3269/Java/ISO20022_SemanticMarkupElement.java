





import java.util.List;
import java.util.ArrayList;

public class ISO20022_SemanticMarkupElement extends ModelEntity {

    private String name;
    private String value;





    private ISO20022_SemanticMarkup iso20022_semanticmarkup;


    public ISO20022_SemanticMarkupElement(
        String name,        String value    ) {
        super(
        );
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public ISO20022_SemanticMarkup getIso20022_semanticmarkup() {
        return iso20022_semanticmarkup;
    }

    public void setIso20022_semanticmarkup(ISO20022_SemanticMarkup iso20022_semanticmarkup) {
        this.iso20022_semanticmarkup = iso20022_semanticmarkup;
    }

}