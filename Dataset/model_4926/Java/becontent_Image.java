





import java.util.List;
import java.util.ArrayList;

public class becontent_Image extends NotStructuredElement {

    private boolean isMandatory;
    private String label;
    private String name;



    public becontent_Image(
        boolean isMandatory,        String label,        String name    ) {
        super(
        );
        this.isMandatory = isMandatory;
        this.label = label;
        this.name = name;
    }


    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
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


}