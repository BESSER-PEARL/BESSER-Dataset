





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_OptionFeatureType extends FeatureType {

    private boolean none;





    private deviceModelingLanguage_BaseFeatureType devicemodelinglanguage_basefeaturetype;


    public deviceModelingLanguage_OptionFeatureType(
        boolean none    ) {
        super(
        );
        this.none = none;
    }


    public boolean getNone() {
        return none;
    }

    public void setNone(boolean none) {
        this.none = none;
    }

    public deviceModelingLanguage_BaseFeatureType getDevicemodelinglanguage_basefeaturetype() {
        return devicemodelinglanguage_basefeaturetype;
    }

    public void setDevicemodelinglanguage_basefeaturetype(deviceModelingLanguage_BaseFeatureType devicemodelinglanguage_basefeaturetype) {
        this.devicemodelinglanguage_basefeaturetype = devicemodelinglanguage_basefeaturetype;
    }

}