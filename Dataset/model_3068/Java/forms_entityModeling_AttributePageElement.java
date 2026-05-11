





import java.util.List;
import java.util.ArrayList;

public class forms_entityModeling_AttributePageElement extends PageElement {

    private String valueOfAttribute;





    private Attribute attribute;


    public forms_entityModeling_AttributePageElement(
        String valueOfAttribute    ) {
        super(
        );
        this.valueOfAttribute = valueOfAttribute;
    }


    public String getValueofattribute() {
        return valueOfAttribute;
    }

    public void setValueofattribute(String valueOfAttribute) {
        this.valueOfAttribute = valueOfAttribute;
    }

    public Attribute getAttribute() {
        return attribute;
    }

    public void setAttribute(Attribute attribute) {
        this.attribute = attribute;
    }

}