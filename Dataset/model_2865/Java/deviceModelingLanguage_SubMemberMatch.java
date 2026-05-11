





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_SubMemberMatch  {

    private String any;
    private String name;
    private String qNames;





    private deviceModelingLanguage_MultiplicityInvariant devicemodelinglanguage_multiplicityinvariant;


    public deviceModelingLanguage_SubMemberMatch(
        String any,        String name,        String qNames    ) {
        this.any = any;
        this.name = name;
        this.qNames = qNames;
    }


    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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