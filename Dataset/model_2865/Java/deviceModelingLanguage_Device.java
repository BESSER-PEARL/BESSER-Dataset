





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_Device extends FeatureDecl {






    private List<deviceModelingLanguage_FeatureDecl> devicemodelinglanguage_featuredecls;




    private deviceModelingLanguage_FeatureDecl devicemodelinglanguage_featuredecl;


    public deviceModelingLanguage_Device(
    ) {
        super(
        );
        this.devicemodelinglanguage_featuredecls = new ArrayList<>();
    }

    public deviceModelingLanguage_Device(
        ArrayList<deviceModelingLanguage_FeatureDecl> devicemodelinglanguage_featuredecls    ) {
        this.devicemodelinglanguage_featuredecls = devicemodelinglanguage_featuredecls;
    }


    public List<deviceModelingLanguage_FeatureDecl> getDevicemodelinglanguage_featuredecls() {
        return devicemodelinglanguage_featuredecls;
    }

    public void addDevicemodelinglanguage_featuredecl(Devicemodelinglanguage_featuredecl devicemodelinglanguage_featuredecl) {
        this.devicemodelinglanguage_featuredecls.add(devicemodelinglanguage_featuredecl);
    }
    public deviceModelingLanguage_FeatureDecl getDevicemodelinglanguage_featuredecl() {
        return devicemodelinglanguage_featuredecl;
    }

    public void setDevicemodelinglanguage_featuredecl(deviceModelingLanguage_FeatureDecl devicemodelinglanguage_featuredecl) {
        this.devicemodelinglanguage_featuredecl = devicemodelinglanguage_featuredecl;
    }

}