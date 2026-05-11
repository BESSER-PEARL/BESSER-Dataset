





import java.util.List;
import java.util.ArrayList;

public class UML_14_Parameter extends ModelElement {

    private String defaultValue;
    private String kind;



    public UML_14_Parameter(
        String defaultValue,        String kind    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.kind = kind;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}