





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_Report  {

    private String name;





    private List<deviceModelingLanguage_Exp> devicemodelinglanguage_exps;


    public deviceModelingLanguage_Report(
        String name    ) {
        this.name = name;
        this.devicemodelinglanguage_exps = new ArrayList<>();
    }

    public deviceModelingLanguage_Report(
        String name        ArrayList<deviceModelingLanguage_Exp> devicemodelinglanguage_exps    ) {
        this.name = name;
        this.devicemodelinglanguage_exps = devicemodelinglanguage_exps;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<deviceModelingLanguage_Exp> getDevicemodelinglanguage_exps() {
        return devicemodelinglanguage_exps;
    }

    public void addDevicemodelinglanguage_exp(Devicemodelinglanguage_exp devicemodelinglanguage_exp) {
        this.devicemodelinglanguage_exps.add(devicemodelinglanguage_exp);
    }

}