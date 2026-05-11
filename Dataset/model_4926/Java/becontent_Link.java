





import java.util.List;
import java.util.ArrayList;

public class becontent_Link extends NotStructuredElement {

    private String label;
    private int size;
    private int maxLength;
    private boolean isMandatory;
    private String name;



    public becontent_Link(
        String label,        int size,        int maxLength,        boolean isMandatory,        String name    ) {
        super(
        );
        this.label = label;
        this.size = size;
        this.maxLength = maxLength;
        this.isMandatory = isMandatory;
        this.name = name;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
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


}