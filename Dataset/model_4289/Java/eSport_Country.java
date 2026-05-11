





import java.util.List;
import java.util.ArrayList;

public class eSport_Country  {

    private String name;





    private eSport_Person esport_person;




    private List<eSport_Tournament> esport_tournaments;




    private eSport_Tournament esport_tournament;




    private List<eSport_Person> esport_persons;


    public eSport_Country(
        String name    ) {
        this.name = name;
        this.esport_tournaments = new ArrayList<>();
        this.esport_persons = new ArrayList<>();
    }

    public eSport_Country(
        String name        ArrayList<eSport_Tournament> esport_tournaments,        ArrayList<eSport_Person> esport_persons    ) {
        this.name = name;
        this.esport_tournaments = esport_tournaments;
        this.esport_persons = esport_persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eSport_Person getEsport_person() {
        return esport_person;
    }

    public void setEsport_person(eSport_Person esport_person) {
        this.esport_person = esport_person;
    }
    public List<eSport_Tournament> getEsport_tournaments() {
        return esport_tournaments;
    }

    public void addEsport_tournament(Esport_tournament esport_tournament) {
        this.esport_tournaments.add(esport_tournament);
    }
    public eSport_Tournament getEsport_tournament() {
        return esport_tournament;
    }

    public void setEsport_tournament(eSport_Tournament esport_tournament) {
        this.esport_tournament = esport_tournament;
    }
    public List<eSport_Person> getEsport_persons() {
        return esport_persons;
    }

    public void addEsport_person(Esport_person esport_person) {
        this.esport_persons.add(esport_person);
    }

}