





import java.util.List;
import java.util.ArrayList;

public class research_team_Software  {

    private String description;
    private String website;
    private String title;





    private research_team_Person research_team_person;




    private List<research_team_Person> research_team_persons;


    public research_team_Software(
        String description,        String website,        String title    ) {
        this.description = description;
        this.website = website;
        this.title = title;
        this.research_team_persons = new ArrayList<>();
    }

    public research_team_Software(
        String description,        String website,        String title        ArrayList<research_team_Person> research_team_persons    ) {
        this.description = description;
        this.website = website;
        this.title = title;
        this.research_team_persons = research_team_persons;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public research_team_Person getResearch_team_person() {
        return research_team_person;
    }

    public void setResearch_team_person(research_team_Person research_team_person) {
        this.research_team_person = research_team_person;
    }
    public List<research_team_Person> getResearch_team_persons() {
        return research_team_persons;
    }

    public void addResearch_team_person(Research_team_person research_team_person) {
        this.research_team_persons.add(research_team_person);
    }

}