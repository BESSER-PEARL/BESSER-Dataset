





import java.util.List;
import java.util.ArrayList;

public class profile_CD  {

    private String codeSystemVersion;
    private String codeSystem;
    private String codeSystemName;
    private String displayName;
    private String code;





    private profile_CD profile_cd;


    public profile_CD(
        String codeSystemVersion,        String codeSystem,        String codeSystemName,        String displayName,        String code    ) {
        this.codeSystemVersion = codeSystemVersion;
        this.codeSystem = codeSystem;
        this.codeSystemName = codeSystemName;
        this.displayName = displayName;
        this.code = code;
    }


    public String getCodesystemversion() {
        return codeSystemVersion;
    }

    public void setCodesystemversion(String codeSystemVersion) {
        this.codeSystemVersion = codeSystemVersion;
    }
    public String getCodesystem() {
        return codeSystem;
    }

    public void setCodesystem(String codeSystem) {
        this.codeSystem = codeSystem;
    }
    public String getCodesystemname() {
        return codeSystemName;
    }

    public void setCodesystemname(String codeSystemName) {
        this.codeSystemName = codeSystemName;
    }
    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public profile_CD getProfile_cd() {
        return profile_cd;
    }

    public void setProfile_cd(profile_CD profile_cd) {
        this.profile_cd = profile_cd;
    }

}