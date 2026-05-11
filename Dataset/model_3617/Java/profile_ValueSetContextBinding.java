





import java.util.List;
import java.util.ArrayList;

public class profile_ValueSetContextBinding  {

    private String effectiveDate;





    private profile_Class profile_class;




    private profile_ValueSetVersion profile_valuesetversion;




    private profile_ConceptDomain profile_conceptdomain;




    private profile_UsageContext profile_usagecontext;


    public profile_ValueSetContextBinding(
        String effectiveDate    ) {
        this.effectiveDate = effectiveDate;
    }


    public String getEffectivedate() {
        return effectiveDate;
    }

    public void setEffectivedate(String effectiveDate) {
        this.effectiveDate = effectiveDate;
    }

    public profile_Class getProfile_class() {
        return profile_class;
    }

    public void setProfile_class(profile_Class profile_class) {
        this.profile_class = profile_class;
    }
    public profile_ValueSetVersion getProfile_valuesetversion() {
        return profile_valuesetversion;
    }

    public void setProfile_valuesetversion(profile_ValueSetVersion profile_valuesetversion) {
        this.profile_valuesetversion = profile_valuesetversion;
    }
    public profile_ConceptDomain getProfile_conceptdomain() {
        return profile_conceptdomain;
    }

    public void setProfile_conceptdomain(profile_ConceptDomain profile_conceptdomain) {
        this.profile_conceptdomain = profile_conceptdomain;
    }
    public profile_UsageContext getProfile_usagecontext() {
        return profile_usagecontext;
    }

    public void setProfile_usagecontext(profile_UsageContext profile_usagecontext) {
        this.profile_usagecontext = profile_usagecontext;
    }

}