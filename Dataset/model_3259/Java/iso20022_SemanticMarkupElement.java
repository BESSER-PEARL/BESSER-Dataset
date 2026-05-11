





import java.util.List;
import java.util.ArrayList;

public class iso20022_SemanticMarkupElement extends ModelEntity {

    private String name;
    private String value;



    public iso20022_SemanticMarkupElement(
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


}