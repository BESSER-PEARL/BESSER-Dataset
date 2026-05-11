





import java.util.List;
import java.util.ArrayList;

public class profile_ValueSetVersion  {

    private String identifier;
    private String version;
    private String fullName;
    private String binding;
    private String expirationDate;
    private String status;
    private String definition;
    private String statusDate;
    private String source;
    private String type;
    private String effectiveDate;
    private String url;
    private String releaseDate;
    private String revisionDate;





    private profile_Enumeration profile_enumeration;




    private profile_ValueSetConstraint profile_valuesetconstraint;


    public profile_ValueSetVersion(
        String identifier,        String version,        String fullName,        String binding,        String expirationDate,        String status,        String definition,        String statusDate,        String source,        String type,        String effectiveDate,        String url,        String releaseDate,        String revisionDate    ) {
        this.identifier = identifier;
        this.version = version;
        this.fullName = fullName;
        this.binding = binding;
        this.expirationDate = expirationDate;
        this.status = status;
        this.definition = definition;
        this.statusDate = statusDate;
        this.source = source;
        this.type = type;
        this.effectiveDate = effectiveDate;
        this.url = url;
        this.releaseDate = releaseDate;
        this.revisionDate = revisionDate;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }
    public String getBinding() {
        return binding;
    }

    public void setBinding(String binding) {
        this.binding = binding;
    }
    public String getExpirationdate() {
        return expirationDate;
    }

    public void setExpirationdate(String expirationDate) {
        this.expirationDate = expirationDate;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getDefinition() {
        return definition;
    }

    public void setDefinition(String definition) {
        this.definition = definition;
    }
    public String getStatusdate() {
        return statusDate;
    }

    public void setStatusdate(String statusDate) {
        this.statusDate = statusDate;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getEffectivedate() {
        return effectiveDate;
    }

    public void setEffectivedate(String effectiveDate) {
        this.effectiveDate = effectiveDate;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getReleasedate() {
        return releaseDate;
    }

    public void setReleasedate(String releaseDate) {
        this.releaseDate = releaseDate;
    }
    public String getRevisiondate() {
        return revisionDate;
    }

    public void setRevisiondate(String revisionDate) {
        this.revisionDate = revisionDate;
    }

    public profile_Enumeration getProfile_enumeration() {
        return profile_enumeration;
    }

    public void setProfile_enumeration(profile_Enumeration profile_enumeration) {
        this.profile_enumeration = profile_enumeration;
    }
    public profile_ValueSetConstraint getProfile_valuesetconstraint() {
        return profile_valuesetconstraint;
    }

    public void setProfile_valuesetconstraint(profile_ValueSetConstraint profile_valuesetconstraint) {
        this.profile_valuesetconstraint = profile_valuesetconstraint;
    }

}