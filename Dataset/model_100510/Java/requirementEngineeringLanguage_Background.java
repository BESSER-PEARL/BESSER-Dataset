





import java.util.List;
import java.util.ArrayList;

public class requirementEngineeringLanguage_Background  {

    private String dashboard;





    private List<requirementEngineeringLanguage_View> requirementengineeringlanguage_views;




    private requirementEngineeringLanguage_Project requirementengineeringlanguage_project;


    public requirementEngineeringLanguage_Background(
        String dashboard    ) {
        this.dashboard = dashboard;
        this.requirementengineeringlanguage_views = new ArrayList<>();
    }

    public requirementEngineeringLanguage_Background(
        String dashboard        ArrayList<requirementEngineeringLanguage_View> requirementengineeringlanguage_views    ) {
        this.dashboard = dashboard;
        this.requirementengineeringlanguage_views = requirementengineeringlanguage_views;
    }

    public String getDashboard() {
        return dashboard;
    }

    public void setDashboard(String dashboard) {
        this.dashboard = dashboard;
    }

    public List<requirementEngineeringLanguage_View> getRequirementengineeringlanguage_views() {
        return requirementengineeringlanguage_views;
    }

    public void addRequirementengineeringlanguage_view(Requirementengineeringlanguage_view requirementengineeringlanguage_view) {
        this.requirementengineeringlanguage_views.add(requirementengineeringlanguage_view);
    }
    public requirementEngineeringLanguage_Project getRequirementengineeringlanguage_project() {
        return requirementengineeringlanguage_project;
    }

    public void setRequirementengineeringlanguage_project(requirementEngineeringLanguage_Project requirementengineeringlanguage_project) {
        this.requirementengineeringlanguage_project = requirementengineeringlanguage_project;
    }

}