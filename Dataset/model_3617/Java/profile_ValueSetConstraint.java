





import java.util.List;
import java.util.ArrayList;

public class profile_ValueSetConstraint  {

    private String name;
    private String extensibility;
    private String guidance;
    private String uri;
    private String binding;
    private String identifier;
    private String version;





    private profile_Property profile_property;


    public profile_ValueSetConstraint(
        String name,        String extensibility,        String guidance,        String uri,        String binding,        String identifier,        String version    ) {
        this.name = name;
        this.extensibility = extensibility;
        this.guidance = guidance;
        this.uri = uri;
        this.binding = binding;
        this.identifier = identifier;
        this.version = version;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getExtensibility() {
        return extensibility;
    }

    public void setExtensibility(String extensibility) {
        this.extensibility = extensibility;
    }
    public String getGuidance() {
        return guidance;
    }

    public void setGuidance(String guidance) {
        this.guidance = guidance;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public String getBinding() {
        return binding;
    }

    public void setBinding(String binding) {
        this.binding = binding;
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

    public profile_Property getProfile_property() {
        return profile_property;
    }

    public void setProfile_property(profile_Property profile_property) {
        this.profile_property = profile_property;
    }

}