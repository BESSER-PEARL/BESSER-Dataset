





import java.util.List;
import java.util.ArrayList;

public class model_profile_Profile extends UnicaseModelElement {






    private List<profile_Stereotype> profile_stereotypes;


    public model_profile_Profile(
    ) {
        super(
        );
        this.profile_stereotypes = new ArrayList<>();
    }

    public model_profile_Profile(
        ArrayList<profile_Stereotype> profile_stereotypes    ) {
        this.profile_stereotypes = profile_stereotypes;
    }


    public List<profile_Stereotype> getProfile_stereotypes() {
        return profile_stereotypes;
    }

    public void addProfile_stereotype(Profile_stereotype profile_stereotype) {
        this.profile_stereotypes.add(profile_stereotype);
    }

}