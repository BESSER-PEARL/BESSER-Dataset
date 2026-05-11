





import java.util.List;
import java.util.ArrayList;

public class metrics_IdentifierDataKind extends DataKind {

    private String pattern;
    private String objectKind;
    private String objectProperty;



    public metrics_IdentifierDataKind(
        String pattern,        String objectKind,        String objectProperty    ) {
        super(
        );
        this.pattern = pattern;
        this.objectKind = objectKind;
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
    public String getObjectproperty() {
        return objectProperty;
    }

    public void setObjectproperty(String objectProperty) {
        this.objectProperty = objectProperty;
    }


}