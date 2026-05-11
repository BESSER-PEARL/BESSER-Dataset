





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_SubMemberMatch  {

    private String name;
    private String any;
    private String qNames;





    private deviceModelingLanguage_MultiplicityInvariant devicemodelinglanguage_multiplicityinvariant;


    public deviceModelingLanguage_SubMemberMatch(
        String name,        String any,        String qNames    ) {
        this.name = name;
        this.any = any;
        this.qNames = qNames;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getQnames() {
        return qNames;
    }

    public void setQnames(String qNames) {
        this.qNames = qNames;
    }

    public deviceModelingLanguage_MultiplicityInvariant getDevicemodelinglanguage_multiplicityinvariant() {
        return devicemodelinglanguage_multiplicityinvariant;
    }

    public void setDevicemodelinglanguage_multiplicityinvariant(deviceModelingLanguage_MultiplicityInvariant devicemodelinglanguage_multiplicityinvariant) {
        this.devicemodelinglanguage_multiplicityinvariant = devicemodelinglanguage_multiplicityinvariant;
    }

}