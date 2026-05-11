





import java.util.List;
import java.util.ArrayList;

public class metrics_IdentifierDataKind extends DataKind {

    private String pattern;
    private String objectProperty;
    private String objectKind;



    public metrics_IdentifierDataKind(
        String pattern,        String objectProperty,        String objectKind    ) {
        super(
        );
        this.pattern = pattern;
        this.objectProperty = objectProperty;
        this.objectKind = objectKind;
    }


    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
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


}