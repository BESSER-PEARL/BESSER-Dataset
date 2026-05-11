





import java.util.List;
import java.util.ArrayList;

public class ccore_Field extends Item {

    private String position;
    private boolean editable;
    private String label;





    private ccore_TypeDefinition ccore_typedefinition;




    private ccore_Attribute ccore_attribute;


    public ccore_Field(
        String position,        boolean editable,        String label    ) {
        super(
        );
        this.position = position;
        this.editable = editable;
        this.label = label;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public boolean getEditable() {
        return editable;
    }

    public void setEditable(boolean editable) {
        this.editable = editable;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public ccore_TypeDefinition getCcore_typedefinition() {
        return ccore_typedefinition;
    }

    public void setCcore_typedefinition(ccore_TypeDefinition ccore_typedefinition) {
        this.ccore_typedefinition = ccore_typedefinition;
    }
    public ccore_Attribute getCcore_attribute() {
        return ccore_attribute;
    }

    public void setCcore_attribute(ccore_Attribute ccore_attribute) {
        this.ccore_attribute = ccore_attribute;
    }

}