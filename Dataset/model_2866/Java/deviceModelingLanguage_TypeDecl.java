





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_TypeDecl extends Decl {






    private List<deviceModelingLanguage_TypeDecl> devicemodelinglanguage_typedecls;


    public deviceModelingLanguage_TypeDecl(
    ) {
        super(
        );
        this.devicemodelinglanguage_typedecls = new ArrayList<>();
    }

    public deviceModelingLanguage_TypeDecl(
        ArrayList<deviceModelingLanguage_TypeDecl> devicemodelinglanguage_typedecls    ) {
        this.devicemodelinglanguage_typedecls = devicemodelinglanguage_typedecls;
    }


    public List<deviceModelingLanguage_TypeDecl> getDevicemodelinglanguage_typedecls() {
        return devicemodelinglanguage_typedecls;
    }

    public void addDevicemodelinglanguage_typedecl(Devicemodelinglanguage_typedecl devicemodelinglanguage_typedecl) {
        this.devicemodelinglanguage_typedecls.add(devicemodelinglanguage_typedecl);
    }

}