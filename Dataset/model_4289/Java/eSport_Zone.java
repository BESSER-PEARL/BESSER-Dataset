





import java.util.List;
import java.util.ArrayList;

public class eSport_Zone  {

    private String name;





    private eSport_Team esport_team;




    private List<eSport_Country> esport_countrys;




    private List<eSport_Tournament> esport_tournaments;




    private eSport_Country esport_country;




    private eSport_Tournament esport_tournament;




    private List<eSport_Team> esport_teams;


    public eSport_Zone(
        String name    ) {
        this.name = name;
        this.esport_countrys = new ArrayList<>();
        this.esport_tournaments = new ArrayList<>();
        this.esport_teams = new ArrayList<>();
    }

    public eSport_Zone(
        String name        ArrayList<eSport_Country> esport_countrys,        ArrayList<eSport_Tournament> esport_tournaments,        ArrayList<eSport_Team> esport_teams    ) {
        this.name = name;
        this.esport_countrys = esport_countrys;
        this.esport_tournaments = esport_tournaments;
        this.esport_teams = esport_teams;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eSport_Team getEsport_team() {
        return esport_team;
    }

    public void setEsport_team(eSport_Team esport_team) {
        this.esport_team = esport_team;
    }
    public List<eSport_Country> getEsport_countrys() {
        return esport_countrys;
    }

    public void addEsport_country(Esport_country esport_country) {
        this.esport_countrys.add(esport_country);
    }
    public List<eSport_Tournament> getEsport_tournaments() {
        return esport_tournaments;
    }

    public void addEsport_tournament(Esport_tournament esport_tournament) {
        this.esport_tournaments.add(esport_tournament);
    }
    public eSport_Country getEsport_country() {
        return esport_country;
    }

    public void setEsport_country(eSport_Country esport_country) {
        this.esport_country = esport_country;
    }
    public eSport_Tournament getEsport_tournament() {
        return esport_tournament;
    }

    public void setEsport_tournament(eSport_Tournament esport_tournament) {
        this.esport_tournament = esport_tournament;
    }
    public List<eSport_Team> getEsport_teams() {
        return esport_teams;
    }

    public void addEsport_team(Esport_team esport_team) {
        this.esport_teams.add(esport_team);
    }

}