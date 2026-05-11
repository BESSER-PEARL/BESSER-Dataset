





import java.util.List;
import java.util.ArrayList;

public class becontent_Password extends NotStructuredElement {

    private boolean isMandatory;
    private String name;
    private String label;
    private int maxLength;
    private int size;



    public becontent_Password(
        boolean isMandatory,        String name,        String label,        int maxLength,        int size    ) {
        super(
        );
        this.isMandatory = isMandatory;
        this.name = name;
        this.label = label;
        this.maxLength = maxLength;
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
    public int getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(int maxLength) {
        this.maxLength = maxLength;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}