





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_Decl  {

    private String name;





    private deviceModelingLanguage_Model devicemodelinglanguage_model;


    public deviceModelingLanguage_Decl(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public deviceModelingLanguage_Model getDevicemodelinglanguage_model() {
        return devicemodelinglanguage_model;
    }

    public void setDevicemodelinglanguage_model(deviceModelingLanguage_Model devicemodelinglanguage_model) {
        this.devicemodelinglanguage_model = devicemodelinglanguage_model;
    }

}