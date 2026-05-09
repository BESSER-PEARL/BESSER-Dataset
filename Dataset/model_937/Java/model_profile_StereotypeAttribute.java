





import java.util.List;
import java.util.ArrayList;

public class model_profile_StereotypeAttribute extends UnicaseModelElement {






    private List<profile_StereotypeAttributeInstance> profile_stereotypeattributeinstances;




    private profile_Stereotype profile_stereotype;


    public model_profile_StereotypeAttribute(
    ) {
        super(
        );
        this.profile_stereotypeattributeinstances = new ArrayList<>();
    }

    public model_profile_StereotypeAttribute(
        ArrayList<profile_StereotypeAttributeInstance> profile_stereotypeattributeinstances    ) {
        this.profile_stereotypeattributeinstances = profile_stereotypeattributeinstances;
    }


    public List<profile_StereotypeAttributeInstance> getProfile_stereotypeattributeinstances() {
        return profile_stereotypeattributeinstances;
    }

    public void addProfile_stereotypeattributeinstance(Profile_stereotypeattributeinstance profile_stereotypeattributeinstance) {
        this.profile_stereotypeattributeinstances.add(profile_stereotypeattributeinstance);
    }
    public profile_Stereotype getProfile_stereotype() {
        return profile_stereotype;
    }

    public void setProfile_stereotype(profile_Stereotype profile_stereotype) {
        this.profile_stereotype = profile_stereotype;
    }

}