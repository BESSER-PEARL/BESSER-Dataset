





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Parameter extends NamedElement {

    private String defaultValue;
    private String kind;





    private uml2CD_PrimitiveType uml2cd_primitivetype;


    public uml2CD_Parameter(
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

    public uml2CD_PrimitiveType getUml2cd_primitivetype() {
        return uml2cd_primitivetype;
    }

    public void setUml2cd_primitivetype(uml2CD_PrimitiveType uml2cd_primitivetype) {
        this.uml2cd_primitivetype = uml2cd_primitivetype;
    }

}