





import java.util.List;
import java.util.ArrayList;

public class profile_CodeSystemConstraint  {

    private String displayName;
    private String version;
    private String identifier;
    private String name;
    private String binding;
    private String code;





    private List<profile_CR> profile_crs;




    private profile_Property profile_property;


    public profile_CodeSystemConstraint(
        String displayName,        String version,        String identifier,        String name,        String binding,        String code    ) {
        this.displayName = displayName;
        this.version = version;
        this.identifier = identifier;
        this.name = name;
        this.binding = binding;
        this.code = code;
        this.profile_crs = new ArrayList<>();
    }

    public profile_CodeSystemConstraint(
        String displayName,        String version,        String identifier,        String name,        String binding,        String code        ArrayList<profile_CR> profile_crs    ) {
        this.displayName = displayName;
        this.version = version;
        this.identifier = identifier;
        this.name = name;
        this.binding = binding;
        this.code = code;
        this.profile_crs = profile_crs;
    }

    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBinding() {
        return binding;
    }

    public void setBinding(String binding) {
        this.binding = binding;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public List<profile_CR> getProfile_crs() {
        return profile_crs;
    }

    public void addProfile_cr(Profile_cr profile_cr) {
        this.profile_crs.add(profile_cr);
    }
    public profile_Property getProfile_property() {
        return profile_property;
    }

    public void setProfile_property(profile_Property profile_property) {
        this.profile_property = profile_property;
    }

}