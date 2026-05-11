





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_Assignment  {

    private String name;





    private deviceModelingLanguage_FeatureDecl devicemodelinglanguage_featuredecl;


    public deviceModelingLanguage_Assignment(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public deviceModelingLanguage_FeatureDecl getDevicemodelinglanguage_featuredecl() {
        return devicemodelinglanguage_featuredecl;
    }

    public void setDevicemodelinglanguage_featuredecl(deviceModelingLanguage_FeatureDecl devicemodelinglanguage_featuredecl) {
        this.devicemodelinglanguage_featuredecl = devicemodelinglanguage_featuredecl;
    }

}