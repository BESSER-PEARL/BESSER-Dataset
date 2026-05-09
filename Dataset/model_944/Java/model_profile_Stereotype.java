





import java.util.List;
import java.util.ArrayList;

public class model_profile_Stereotype extends UnicaseModelElement {

    private boolean required;





    private List<profile_StereotypeInstance> profile_stereotypeinstances;


    public model_profile_Stereotype(
        boolean required    ) {
        super(
        );
        this.required = required;
        this.profile_stereotypeinstances = new ArrayList<>();
    }

    public model_profile_Stereotype(
        boolean required        ArrayList<profile_StereotypeInstance> profile_stereotypeinstances    ) {
        this.required = required;
        this.profile_stereotypeinstances = profile_stereotypeinstances;
    }

    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }

    public List<profile_StereotypeInstance> getProfile_stereotypeinstances() {
        return profile_stereotypeinstances;
    }

    public void addProfile_stereotypeinstance(Profile_stereotypeinstance profile_stereotypeinstance) {
        this.profile_stereotypeinstances.add(profile_stereotypeinstance);
    }

}