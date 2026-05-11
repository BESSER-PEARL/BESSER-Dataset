





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_SetFeatureType extends FeatureType {






    private List<deviceModelingLanguage_BaseFeatureType> devicemodelinglanguage_basefeaturetypes;




    private deviceModelingLanguage_BaseFeatureType devicemodelinglanguage_basefeaturetype;


    public deviceModelingLanguage_SetFeatureType(
    ) {
        super(
        );
        this.devicemodelinglanguage_basefeaturetypes = new ArrayList<>();
    }

    public deviceModelingLanguage_SetFeatureType(
        ArrayList<deviceModelingLanguage_BaseFeatureType> devicemodelinglanguage_basefeaturetypes    ) {
        this.devicemodelinglanguage_basefeaturetypes = devicemodelinglanguage_basefeaturetypes;
    }


    public List<deviceModelingLanguage_BaseFeatureType> getDevicemodelinglanguage_basefeaturetypes() {
        return devicemodelinglanguage_basefeaturetypes;
    }

    public void addDevicemodelinglanguage_basefeaturetype(Devicemodelinglanguage_basefeaturetype devicemodelinglanguage_basefeaturetype) {
        this.devicemodelinglanguage_basefeaturetypes.add(devicemodelinglanguage_basefeaturetype);
    }
    public deviceModelingLanguage_BaseFeatureType getDevicemodelinglanguage_basefeaturetype() {
        return devicemodelinglanguage_basefeaturetype;
    }

    public void setDevicemodelinglanguage_basefeaturetype(deviceModelingLanguage_BaseFeatureType devicemodelinglanguage_basefeaturetype) {
        this.devicemodelinglanguage_basefeaturetype = devicemodelinglanguage_basefeaturetype;
    }

}