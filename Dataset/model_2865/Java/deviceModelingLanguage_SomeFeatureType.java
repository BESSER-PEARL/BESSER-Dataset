





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_SomeFeatureType extends FeatureType {






    private List<deviceModelingLanguage_MemberDecl> devicemodelinglanguage_memberdecls;




    private deviceModelingLanguage_BaseFeatureType devicemodelinglanguage_basefeaturetype;


    public deviceModelingLanguage_SomeFeatureType(
    ) {
        super(
        );
        this.devicemodelinglanguage_memberdecls = new ArrayList<>();
    }

    public deviceModelingLanguage_SomeFeatureType(
        ArrayList<deviceModelingLanguage_MemberDecl> devicemodelinglanguage_memberdecls    ) {
        this.devicemodelinglanguage_memberdecls = devicemodelinglanguage_memberdecls;
    }


    public List<deviceModelingLanguage_MemberDecl> getDevicemodelinglanguage_memberdecls() {
        return devicemodelinglanguage_memberdecls;
    }

    public void addDevicemodelinglanguage_memberdecl(Devicemodelinglanguage_memberdecl devicemodelinglanguage_memberdecl) {
        this.devicemodelinglanguage_memberdecls.add(devicemodelinglanguage_memberdecl);
    }
    public deviceModelingLanguage_BaseFeatureType getDevicemodelinglanguage_basefeaturetype() {
        return devicemodelinglanguage_basefeaturetype;
    }

    public void setDevicemodelinglanguage_basefeaturetype(deviceModelingLanguage_BaseFeatureType devicemodelinglanguage_basefeaturetype) {
        this.devicemodelinglanguage_basefeaturetype = devicemodelinglanguage_basefeaturetype;
    }

}