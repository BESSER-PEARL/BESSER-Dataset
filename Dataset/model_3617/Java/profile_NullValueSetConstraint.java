





import java.util.List;
import java.util.ArrayList;

public class profile_NullValueSetConstraint  {

    private String version;
    private String binding;
    private String name;
    private String identifier;





    private profile_Property profile_property;




    private profile_ValueSetVersion profile_valuesetversion;


    public profile_NullValueSetConstraint(
        String version,        String binding,        String name,        String identifier    ) {
        this.version = version;
        this.binding = binding;
        this.name = name;
        this.identifier = identifier;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getBinding() {
        return binding;
    }

    public void setBinding(String binding) {
        this.binding = binding;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public profile_Property getProfile_property() {
        return profile_property;
    }

    public void setProfile_property(profile_Property profile_property) {
        this.profile_property = profile_property;
    }
    public profile_ValueSetVersion getProfile_valuesetversion() {
        return profile_valuesetversion;
    }

    public void setProfile_valuesetversion(profile_ValueSetVersion profile_valuesetversion) {
        this.profile_valuesetversion = profile_valuesetversion;
    }

}