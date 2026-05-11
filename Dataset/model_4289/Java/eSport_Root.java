





import java.util.List;
import java.util.ArrayList;

public class eSport_Root  {






    private List<eSport_Tournament> esport_tournaments;




    private List<eSport_Person> esport_persons;




    private List<eSport_Zone> esport_zones;




    private List<eSport_Qualification> esport_qualifications;




    private List<eSport_Team> esport_teams;




    private List<eSport_Country> esport_countrys;




    private List<eSport_League> esport_leagues;


    public eSport_Root(
    ) {
        this.esport_tournaments = new ArrayList<>();
        this.esport_persons = new ArrayList<>();
        this.esport_zones = new ArrayList<>();
        this.esport_qualifications = new ArrayList<>();
        this.esport_teams = new ArrayList<>();
        this.esport_countrys = new ArrayList<>();
        this.esport_leagues = new ArrayList<>();
    }

    public eSport_Root(
        ArrayList<eSport_Tournament> esport_tournaments,        ArrayList<eSport_Person> esport_persons,        ArrayList<eSport_Zone> esport_zones,        ArrayList<eSport_Qualification> esport_qualifications,        ArrayList<eSport_Team> esport_teams,        ArrayList<eSport_Country> esport_countrys,        ArrayList<eSport_League> esport_leagues    ) {
        this.esport_tournaments = esport_tournaments;
        this.esport_persons = esport_persons;
        this.esport_zones = esport_zones;
        this.esport_qualifications = esport_qualifications;
        this.esport_teams = esport_teams;
        this.esport_countrys = esport_countrys;
        this.esport_leagues = esport_leagues;
    }


    public List<eSport_Tournament> getEsport_tournaments() {
        return esport_tournaments;
    }

    public void addEsport_tournament(Esport_tournament esport_tournament) {
        this.esport_tournaments.add(esport_tournament);
    }
    public List<eSport_Person> getEsport_persons() {
        return esport_persons;
    }

    public void addEsport_person(Esport_person esport_person) {
        this.esport_persons.add(esport_person);
    }
    public List<eSport_Zone> getEsport_zones() {
        return esport_zones;
    }

    public void addEsport_zone(Esport_zone esport_zone) {
        this.esport_zones.add(esport_zone);
    }
    public List<eSport_Qualification> getEsport_qualifications() {
        return esport_qualifications;
    }

    public void addEsport_qualification(Esport_qualification esport_qualification) {
        this.esport_qualifications.add(esport_qualification);
    }
    public List<eSport_Team> getEsport_teams() {
        return esport_teams;
    }

    public void addEsport_team(Esport_team esport_team) {
        this.esport_teams.add(esport_team);
    }
    public List<eSport_Country> getEsport_countrys() {
        return esport_countrys;
    }

    public void addEsport_country(Esport_country esport_country) {
        this.esport_countrys.add(esport_country);
    }
    public List<eSport_League> getEsport_leagues() {
        return esport_leagues;
    }

    public void addEsport_league(Esport_league esport_league) {
        this.esport_leagues.add(esport_league);
    }

}