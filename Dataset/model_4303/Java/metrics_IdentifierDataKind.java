





import java.util.List;
import java.util.ArrayList;

public class metrics_IdentifierDataKind extends DataKind {

    private String objectProperty;
    private String objectKind;
    private String pattern;



    public metrics_IdentifierDataKind(
        String objectProperty,        String objectKind,        String pattern    ) {
        super(
        );
        this.objectProperty = objectProperty;
        this.objectKind = objectKind;
        this.pattern = pattern;
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
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }


}