





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_BasicLiteral extends Literal {

    private String lit;





    private deviceModelingLanguage_TypeDecl devicemodelinglanguage_typedecl;


    public deviceModelingLanguage_BasicLiteral(
        String lit    ) {
        super(
        );
        this.lit = lit;
    }


    public String getLit() {
        return lit;
    }

    public void setLit(String lit) {
        this.lit = lit;
    }

    public deviceModelingLanguage_TypeDecl getDevicemodelinglanguage_typedecl() {
        return devicemodelinglanguage_typedecl;
    }

    public void setDevicemodelinglanguage_typedecl(deviceModelingLanguage_TypeDecl devicemodelinglanguage_typedecl) {
        this.devicemodelinglanguage_typedecl = devicemodelinglanguage_typedecl;
    }

}