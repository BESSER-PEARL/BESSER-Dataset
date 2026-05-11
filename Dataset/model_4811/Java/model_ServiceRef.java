





import java.util.List;
import java.util.ArrayList;

public class model_ServiceRef extends ExtensibleElement {

    private String value;
    private String referenceScheme;





    private model_From model_from;


    public model_ServiceRef(
        String value,        String referenceScheme    ) {
        super(
        );
        this.value = value;
        this.referenceScheme = referenceScheme;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getReferencescheme() {
        return referenceScheme;
    }

    public void setReferencescheme(String referenceScheme) {
        this.referenceScheme = referenceScheme;
    }

    public model_From getModel_from() {
        return model_from;
    }

    public void setModel_from(model_From model_from) {
        this.model_from = model_from;
    }

}