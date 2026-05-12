





import java.util.List;
import java.util.ArrayList;

public class research_team_Seminar  {

    private String title;
    private String dateUntil;
    private String dateFrom;
    private String place;
    private String url4slides;
    private String abstract;





    private research_team_Person research_team_person;




    private List<research_team_Person> research_team_persons;


    public research_team_Seminar(
        String title,        String dateUntil,        String dateFrom,        String place,        String url4slides,        String abstract    ) {
        this.title = title;
        this.dateUntil = dateUntil;
        this.dateFrom = dateFrom;
        this.place = place;
        this.url4slides = url4slides;
        this.abstract = abstract;
        this.research_team_persons = new ArrayList<>();
    }

    public research_team_Seminar(
        String title,        String dateUntil,        String dateFrom,        String place,        String url4slides,        String abstract        ArrayList<research_team_Person> research_team_persons    ) {
        this.title = title;
        this.dateUntil = dateUntil;
        this.dateFrom = dateFrom;
        this.place = place;
        this.url4slides = url4slides;
        this.abstract = abstract;
        this.research_team_persons = research_team_persons;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getDateuntil() {
        return dateUntil;
    }

    public void setDateuntil(String dateUntil) {
        this.dateUntil = dateUntil;
    }
    public String getDatefrom() {
        return dateFrom;
    }

    public void setDatefrom(String dateFrom) {
        this.dateFrom = dateFrom;
    }
    public String getPlace() {
        return place;
    }

    public void setPlace(String place) {
        this.place = place;
    }
    public String getUrl4slides() {
        return url4slides;
    }

    public void setUrl4slides(String url4slides) {
        this.url4slides = url4slides;
    }
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
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