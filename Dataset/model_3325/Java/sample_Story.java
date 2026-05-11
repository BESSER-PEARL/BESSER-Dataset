





import java.util.List;
import java.util.ArrayList;

public class sample_Story  {

    private String Feature;
    private String Title;
    private String Role;
    private String Benefit;





    private List<sample_Scenario> sample_scenarios;


    public sample_Story(
        String Feature,        String Title,        String Role,        String Benefit    ) {
        this.Feature = Feature;
        this.Title = Title;
        this.Role = Role;
        this.Benefit = Benefit;
        this.sample_scenarios = new ArrayList<>();
    }

    public sample_Story(
        String Feature,        String Title,        String Role,        String Benefit        ArrayList<sample_Scenario> sample_scenarios    ) {
        this.Feature = Feature;
        this.Title = Title;
        this.Role = Role;
        this.Benefit = Benefit;
        this.sample_scenarios = sample_scenarios;
    }

    public String getFeature() {
        return Feature;
    }

    public void setFeature(String Feature) {
        this.Feature = Feature;
    }
    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }
    public String getRole() {
        return Role;
    }

    public void setRole(String Role) {
        this.Role = Role;
    }
    public String getBenefit() {
        return Benefit;
    }

    public void setBenefit(String Benefit) {
        this.Benefit = Benefit;
    }

    public List<sample_Scenario> getSample_scenarios() {
        return sample_scenarios;
    }

    public void addSample_scenario(Sample_scenario sample_scenario) {
        this.sample_scenarios.add(sample_scenario);
    }

}