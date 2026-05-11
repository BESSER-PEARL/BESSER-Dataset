





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_Model  {






    private List<reqLanguage_Requirement> reqlanguage_requirements;


    public reqLanguage_Model(
    ) {
        this.reqlanguage_requirements = new ArrayList<>();
    }

    public reqLanguage_Model(
        ArrayList<reqLanguage_Requirement> reqlanguage_requirements    ) {
        this.reqlanguage_requirements = reqlanguage_requirements;
    }


    public List<reqLanguage_Requirement> getReqlanguage_requirements() {
        return reqlanguage_requirements;
    }

    public void addReqlanguage_requirement(Reqlanguage_requirement reqlanguage_requirement) {
        this.reqlanguage_requirements.add(reqlanguage_requirement);
    }

}