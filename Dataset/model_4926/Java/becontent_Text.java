





import java.util.List;
import java.util.ArrayList;

public class becontent_Text extends NotStructuredElement {

    private String label;
    private String name;
    private boolean isMandatory;
    private int size;
    private int maxLength;



    public becontent_Text(
        String label,        String name,        boolean isMandatory,        int size,        int maxLength    ) {
        super(
        );
        this.label = label;
        this.name = name;
        this.isMandatory = isMandatory;
        this.size = size;
        this.maxLength = maxLength;
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
    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public int getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(int maxLength) {
        this.maxLength = maxLength;
    }


}