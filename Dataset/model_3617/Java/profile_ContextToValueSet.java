





import java.util.List;
import java.util.ArrayList;

public class profile_ContextToValueSet  {

    private String key;
    private String value;





    private profile_ValueSetConstraints profile_valuesetconstraints;


    public profile_ContextToValueSet(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public profile_ValueSetConstraints getProfile_valuesetconstraints() {
        return profile_valuesetconstraints;
    }

    public void setProfile_valuesetconstraints(profile_ValueSetConstraints profile_valuesetconstraints) {
        this.profile_valuesetconstraints = profile_valuesetconstraints;
    }

}