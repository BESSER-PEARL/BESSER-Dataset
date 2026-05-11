





import java.util.List;
import java.util.ArrayList;

public class metrics_IdentifierDataKind extends DataKind {

    private String objectProperty;
    private String objectKind;



    public metrics_IdentifierDataKind(
        String objectProperty,        String objectKind    ) {
        super(
        );
        this.objectProperty = objectProperty;
        this.objectKind = objectKind;
    }


    public String getObjectproperty() {
        return objectProperty;
    }

    public void setObjectproperty(String objectProperty) {
        this.objectProperty = objectProperty;
    }
    public String getObjectkind() {
        return objectKind;
    }

    public void setObjectkind(String objectKind) {
        this.objectKind = objectKind;
    }


}