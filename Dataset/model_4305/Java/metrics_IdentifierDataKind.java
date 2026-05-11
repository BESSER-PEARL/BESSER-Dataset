





import java.util.List;
import java.util.ArrayList;

public class metrics_IdentifierDataKind extends DataKind {

    private String objectKind;
    private String pattern;
    private String objectProperty;



    public metrics_IdentifierDataKind(
        String objectKind,        String pattern,        String objectProperty    ) {
        super(
        );
        this.objectKind = objectKind;
        this.pattern = pattern;
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
    public String getObjectproperty() {
        return objectProperty;
    }

    public void setObjectproperty(String objectProperty) {
        this.objectProperty = objectProperty;
    }


}