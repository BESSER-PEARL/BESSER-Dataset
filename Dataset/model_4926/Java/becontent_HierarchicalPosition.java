





import java.util.List;
import java.util.ArrayList;

public class becontent_HierarchicalPosition extends NotStructuredElement {

    private String referenceField;
    private String label;
    private String name;
    private int size;
    private String controlledField;



    public becontent_HierarchicalPosition(
        String referenceField,        String label,        String name,        int size,        String controlledField    ) {
        super(
        );
        this.referenceField = referenceField;
        this.label = label;
        this.name = name;
        this.size = size;
        this.controlledField = controlledField;
    }


    public String getReferencefield() {
        return referenceField;
    }

    public void setReferencefield(String referenceField) {
        this.referenceField = referenceField;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getControlledfield() {
        return controlledField;
    }

    public void setControlledfield(String controlledField) {
        this.controlledField = controlledField;
    }


}