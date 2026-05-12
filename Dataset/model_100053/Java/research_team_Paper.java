





import java.util.List;
import java.util.ArrayList;

public class research_team_Paper  {

    private String state;
    private String title;
    private String url4pdf;





    private List<research_team_Publication> research_team_publications;




    private research_team_Publication research_team_publication;




    private List<research_team_Person> research_team_persons;




    private research_team_Person research_team_person;


    public research_team_Paper(
        String state,        String title,        String url4pdf    ) {
        this.state = state;
        this.title = title;
        this.url4pdf = url4pdf;
        this.research_team_publications = new ArrayList<>();
        this.research_team_persons = new ArrayList<>();
    }

    public research_team_Paper(
        String state,        String title,        String url4pdf        ArrayList<research_team_Publication> research_team_publications,        ArrayList<research_team_Person> research_team_persons    ) {
        this.state = state;
        this.title = title;
        this.url4pdf = url4pdf;
        this.research_team_publications = research_team_publications;
        this.research_team_persons = research_team_persons;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getUrl4pdf() {
        return url4pdf;
    }

    public void setUrl4pdf(String url4pdf) {
        this.url4pdf = url4pdf;
    }

    public List<research_team_Publication> getResearch_team_publications() {
        return research_team_publications;
    }

    public void addResearch_team_publication(Research_team_publication research_team_publication) {
        this.research_team_publications.add(research_team_publication);
    }
    public research_team_Publication getResearch_team_publication() {
        return research_team_publication;
    }

    public void setResearch_team_publication(research_team_Publication research_team_publication) {
        this.research_team_publication = research_team_publication;
    }
    public List<research_team_Person> getResearch_team_persons() {
        return research_team_persons;
    }

    public void addResearch_team_person(Research_team_person research_team_person) {
        this.research_team_persons.add(research_team_person);
    }
    public research_team_Person getResearch_team_person() {
        return research_team_person;
    }

    public void setResearch_team_person(research_team_Person research_team_person) {
        this.research_team_person = research_team_person;
    }

}