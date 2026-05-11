





import java.util.List;
import java.util.ArrayList;

public class becontent_Checkbox extends NotStructuredElement {

    private String name;
    private String label;
    private boolean isChecked;
    private String value;



    public becontent_Checkbox(
        String name,        String label,        boolean isChecked,        String value    ) {
        super(
        );
        this.name = name;
        this.label = label;
        this.isChecked = isChecked;
        this.value = value;
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
    public boolean getIschecked() {
        return isChecked;
    }

    public void setIschecked(boolean isChecked) {
        this.isChecked = isChecked;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}