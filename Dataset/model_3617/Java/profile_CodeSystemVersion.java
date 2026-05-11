





import java.util.List;
import java.util.ArrayList;

public class profile_CodeSystemVersion  {

    private String source;
    private String statusDate;
    private String version;
    private String status;
    private String fullName;
    private String url;
    private String effectiveDate;
    private String releaseDate;
    private String identifier;





    private profile_CodeSystemConstraint profile_codesystemconstraint;




    private profile_Enumeration profile_enumeration;




    private profile_ValueSetVersion profile_valuesetversion;


    public profile_CodeSystemVersion(
        String source,        String statusDate,        String version,        String status,        String fullName,        String url,        String effectiveDate,        String releaseDate,        String identifier    ) {
        this.source = source;
        this.statusDate = statusDate;
        this.version = version;
        this.status = status;
        this.fullName = fullName;
        this.url = url;
        this.effectiveDate = effectiveDate;
        this.releaseDate = releaseDate;
        this.identifier = identifier;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getStatusdate() {
        return statusDate;
    }

    public void setStatusdate(String statusDate) {
        this.statusDate = statusDate;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getEffectivedate() {
        return effectiveDate;
    }

    public void setEffectivedate(String effectiveDate) {
        this.effectiveDate = effectiveDate;
    }
    public String getReleasedate() {
        return releaseDate;
    }

    public void setReleasedate(String releaseDate) {
        this.releaseDate = releaseDate;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public profile_CodeSystemConstraint getProfile_codesystemconstraint() {
        return profile_codesystemconstraint;
    }

    public void setProfile_codesystemconstraint(profile_CodeSystemConstraint profile_codesystemconstraint) {
        this.profile_codesystemconstraint = profile_codesystemconstraint;
    }
    public profile_Enumeration getProfile_enumeration() {
        return profile_enumeration;
    }

    public void setProfile_enumeration(profile_Enumeration profile_enumeration) {
        this.profile_enumeration = profile_enumeration;
    }
    public profile_ValueSetVersion getProfile_valuesetversion() {
        return profile_valuesetversion;
    }

    public void setProfile_valuesetversion(profile_ValueSetVersion profile_valuesetversion) {
        this.profile_valuesetversion = profile_valuesetversion;
    }

}