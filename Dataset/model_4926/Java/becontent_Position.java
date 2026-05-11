





import java.util.List;
import java.util.ArrayList;

public class becontent_Position extends NotStructuredElement {

    private boolean isMandatory;
    private String name;
    private String label;
    private String controlledField;
    private int size;



    public becontent_Position(
        boolean isMandatory,        String name,        String label,        String controlledField,        int size    ) {
        super(
        );
        this.isMandatory = isMandatory;
        this.name = name;
        this.label = label;
        this.controlledField = controlledField;
        this.size = size;
    }


    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getControlledfield() {
        return controlledField;
    }

    public void setControlledfield(String controlledField) {
        this.controlledField = controlledField;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}