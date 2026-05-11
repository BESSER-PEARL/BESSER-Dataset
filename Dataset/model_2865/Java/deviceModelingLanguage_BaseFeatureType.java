





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_BaseFeatureType extends FeatureType {






    private List<deviceModelingLanguage_FeatureDecl> devicemodelinglanguage_featuredecls;




    private List<deviceModelingLanguage_MemberDecl> devicemodelinglanguage_memberdecls;


    public deviceModelingLanguage_BaseFeatureType(
    ) {
        super(
        );
        this.devicemodelinglanguage_featuredecls = new ArrayList<>();
        this.devicemodelinglanguage_memberdecls = new ArrayList<>();
    }

    public deviceModelingLanguage_BaseFeatureType(
        ArrayList<deviceModelingLanguage_FeatureDecl> devicemodelinglanguage_featuredecls,        ArrayList<deviceModelingLanguage_MemberDecl> devicemodelinglanguage_memberdecls    ) {
        this.devicemodelinglanguage_featuredecls = devicemodelinglanguage_featuredecls;
        this.devicemodelinglanguage_memberdecls = devicemodelinglanguage_memberdecls;
    }


    public List<deviceModelingLanguage_FeatureDecl> getDevicemodelinglanguage_featuredecls() {
        return devicemodelinglanguage_featuredecls;
    }

    public void addDevicemodelinglanguage_featuredecl(Devicemodelinglanguage_featuredecl devicemodelinglanguage_featuredecl) {
        this.devicemodelinglanguage_featuredecls.add(devicemodelinglanguage_featuredecl);
    }
    public List<deviceModelingLanguage_MemberDecl> getDevicemodelinglanguage_memberdecls() {
        return devicemodelinglanguage_memberdecls;
    }

    public void addDevicemodelinglanguage_memberdecl(Devicemodelinglanguage_memberdecl devicemodelinglanguage_memberdecl) {
        this.devicemodelinglanguage_memberdecls.add(devicemodelinglanguage_memberdecl);
    }

}