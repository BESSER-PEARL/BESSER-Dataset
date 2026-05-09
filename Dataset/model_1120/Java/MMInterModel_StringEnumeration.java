





import java.util.List;
import java.util.ArrayList;

public class MMInterModel_StringEnumeration extends Element {

    private String attribute;





    private MMInterModel_Attribute mmintermodel_attribute;


    public MMInterModel_StringEnumeration(
        String attribute    ) {
        super(
        );
        this.attribute = attribute;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public MMInterModel_Attribute getMmintermodel_attribute() {
        return mmintermodel_attribute;
    }

    public void setMmintermodel_attribute(MMInterModel_Attribute mmintermodel_attribute) {
        this.mmintermodel_attribute = mmintermodel_attribute;
    }

}