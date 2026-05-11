





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_EitherFeatureType extends FeatureType {

    private String choice;





    private List<deviceModelingLanguage_BaseFeatureType> devicemodelinglanguage_basefeaturetypes;




    private List<deviceModelingLanguage_MemberDecl> devicemodelinglanguage_memberdecls;


    public deviceModelingLanguage_EitherFeatureType(
        String choice    ) {
        super(
        );
        this.choice = choice;
        this.devicemodelinglanguage_basefeaturetypes = new ArrayList<>();
        this.devicemodelinglanguage_memberdecls = new ArrayList<>();
    }

    public deviceModelingLanguage_EitherFeatureType(
        String choice        ArrayList<deviceModelingLanguage_BaseFeatureType> devicemodelinglanguage_basefeaturetypes,        ArrayList<deviceModelingLanguage_MemberDecl> devicemodelinglanguage_memberdecls    ) {
        this.choice = choice;
        this.devicemodelinglanguage_basefeaturetypes = devicemodelinglanguage_basefeaturetypes;
        this.devicemodelinglanguage_memberdecls = devicemodelinglanguage_memberdecls;
    }

    public String getChoice() {
        return choice;
    }

    public void setChoice(String choice) {
        this.choice = choice;
    }

    public List<deviceModelingLanguage_BaseFeatureType> getDevicemodelinglanguage_basefeaturetypes() {
        return devicemodelinglanguage_basefeaturetypes;
    }

    public void addDevicemodelinglanguage_basefeaturetype(Devicemodelinglanguage_basefeaturetype devicemodelinglanguage_basefeaturetype) {
        this.devicemodelinglanguage_basefeaturetypes.add(devicemodelinglanguage_basefeaturetype);
    }
    public List<deviceModelingLanguage_MemberDecl> getDevicemodelinglanguage_memberdecls() {
        return devicemodelinglanguage_memberdecls;
    }

    public void addDevicemodelinglanguage_memberdecl(Devicemodelinglanguage_memberdecl devicemodelinglanguage_memberdecl) {
        this.devicemodelinglanguage_memberdecls.add(devicemodelinglanguage_memberdecl);
    }

}