





import java.util.List;
import java.util.ArrayList;

public class profile_ValueSetCode  {

    private String usageNote;
    private String conceptName;





    private profile_CodeSystemVersion profile_codesystemversion;


    public profile_ValueSetCode(
        String usageNote,        String conceptName    ) {
        this.usageNote = usageNote;
        this.conceptName = conceptName;
    }


    public String getUsagenote() {
        return usageNote;
    }

    public void setUsagenote(String usageNote) {
        this.usageNote = usageNote;
    }
    public String getConceptname() {
        return conceptName;
    }

    public void setConceptname(String conceptName) {
        this.conceptName = conceptName;
    }

    public profile_CodeSystemVersion getProfile_codesystemversion() {
        return profile_codesystemversion;
    }

    public void setProfile_codesystemversion(profile_CodeSystemVersion profile_codesystemversion) {
        this.profile_codesystemversion = profile_codesystemversion;
    }

}