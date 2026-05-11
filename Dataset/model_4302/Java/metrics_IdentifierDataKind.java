





import java.util.List;
import java.util.ArrayList;

public class metrics_IdentifierDataKind extends DataKind {

    private String objectProperty;
    private String pattern;
    private String objectKind;



    public metrics_IdentifierDataKind(
        String objectProperty,        String pattern,        String objectKind    ) {
        super(
        );
        this.objectProperty = objectProperty;
        this.pattern = pattern;
        this.objectKind = objectKind;
    }


    public String getObjectproperty() {
        return objectProperty;
    }

    public void setObjectproperty(String objectProperty) {
        this.objectProperty = objectProperty;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public String getObjectkind() {
        return objectKind;
    }

    public void setObjectkind(String objectKind) {
        this.objectKind = objectKind;
    }


}