





import java.util.List;
import java.util.ArrayList;

public class requirementEngineeringLanguage_Feature  {

    private String name;
    private String desc;





    private List<requirementEngineeringLanguage_Scenario> requirementengineeringlanguage_scenarios;




    private requirementEngineeringLanguage_Project requirementengineeringlanguage_project;


    public requirementEngineeringLanguage_Feature(
        String name,        String desc    ) {
        this.name = name;
        this.desc = desc;
        this.requirementengineeringlanguage_scenarios = new ArrayList<>();
    }

    public requirementEngineeringLanguage_Feature(
        String name,        String desc        ArrayList<requirementEngineeringLanguage_Scenario> requirementengineeringlanguage_scenarios    ) {
        this.name = name;
        this.desc = desc;
        this.requirementengineeringlanguage_scenarios = requirementengineeringlanguage_scenarios;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }

    public List<requirementEngineeringLanguage_Scenario> getRequirementengineeringlanguage_scenarios() {
        return requirementengineeringlanguage_scenarios;
    }

    public void addRequirementengineeringlanguage_scenario(Requirementengineeringlanguage_scenario requirementengineeringlanguage_scenario) {
        this.requirementengineeringlanguage_scenarios.add(requirementengineeringlanguage_scenario);
    }
    public requirementEngineeringLanguage_Project getRequirementengineeringlanguage_project() {
        return requirementengineeringlanguage_project;
    }

    public void setRequirementengineeringlanguage_project(requirementEngineeringLanguage_Project requirementengineeringlanguage_project) {
        this.requirementengineeringlanguage_project = requirementengineeringlanguage_project;
    }

}