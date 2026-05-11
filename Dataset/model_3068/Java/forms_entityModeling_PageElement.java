





import java.util.List;
import java.util.ArrayList;

public class forms_entityModeling_PageElement  {

    private String label;
    private String elementID;





    private Condition condition;


    public forms_entityModeling_PageElement(
        String label,        String elementID    ) {
        this.label = label;
        this.elementID = elementID;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getElementid() {
        return elementID;
    }

    public void setElementid(String elementID) {
        this.elementID = elementID;
    }

    public Condition getCondition() {
        return condition;
    }

    public void setCondition(Condition condition) {
        this.condition = condition;
    }

}