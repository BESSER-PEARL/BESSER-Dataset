





import java.util.List;
import java.util.ArrayList;

public class becontent_RadioButton extends NotStructuredElement {

    private String values;
    private String name;
    private String label;



    public becontent_RadioButton(
        String values,        String name,        String label    ) {
        super(
        );
        this.values = values;
        this.name = name;
        this.label = label;
    }


    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
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


}