





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Parameter  {

    private String defaultValue;
    private String kind;



    public uml2CD_Parameter(
        String defaultValue,        String kind    ) {
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