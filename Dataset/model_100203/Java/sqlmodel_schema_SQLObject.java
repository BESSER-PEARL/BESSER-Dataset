





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_schema_SQLObject extends ENamedElement {

    private String label;
    private String description;



    public sqlmodel_schema_SQLObject(
        String label,        String description    ) {
        super(
        );
        this.label = label;
        this.description = description;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}