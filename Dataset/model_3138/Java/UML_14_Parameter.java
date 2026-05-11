





import java.util.List;
import java.util.ArrayList;

public class UML_14_Parameter extends ModelElement {

    private String kind;
    private String defaultValue;



    public UML_14_Parameter(
        String kind,        String defaultValue    ) {
        super(
        );
        this.kind = kind;
        this.defaultValue = defaultValue;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }


}