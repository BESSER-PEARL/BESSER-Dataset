





import java.util.List;
import java.util.ArrayList;

public class research_team_Partner  {

    private String category;
    private String name;
    private String country;





    private List<research_team_Collaboration> research_team_collaborations;


    public research_team_Partner(
        String category,        String name,        String country    ) {
        this.category = category;
        this.name = name;
        this.country = country;
        this.research_team_collaborations = new ArrayList<>();
    }

    public research_team_Partner(
        String category,        String name,        String country        ArrayList<research_team_Collaboration> research_team_collaborations    ) {
        this.category = category;
        this.name = name;
        this.country = country;
        this.research_team_collaborations = research_team_collaborations;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public List<research_team_Collaboration> getResearch_team_collaborations() {
        return research_team_collaborations;
    }

    public void addResearch_team_collaboration(Research_team_collaboration research_team_collaboration) {
        this.research_team_collaborations.add(research_team_collaboration);
    }

}