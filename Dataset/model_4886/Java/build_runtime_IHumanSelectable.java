





import java.util.List;
import java.util.ArrayList;

public class build_runtime_IHumanSelectable extends IExtension {

    private String typeName;
    private String label;



    public build_runtime_IHumanSelectable(
        String typeName,        String label    ) {
        super(
        );
        this.typeName = typeName;
        this.label = label;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}