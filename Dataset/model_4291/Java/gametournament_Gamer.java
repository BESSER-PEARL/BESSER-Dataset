





import java.util.List;
import java.util.ArrayList;

public class gametournament_Gamer  {

    private String lastName;
    private String firstName;
    private String pseudo;
    private int matches;
    private int victories;





    private gametournament_Tournament gametournament_tournament;


    public gametournament_Gamer(
        String lastName,        String firstName,        String pseudo,        int matches,        int victories    ) {
        this.lastName = lastName;
        this.firstName = firstName;
        this.pseudo = pseudo;
        this.matches = matches;
        this.victories = victories;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getPseudo() {
        return pseudo;
    }

    public void setPseudo(String pseudo) {
        this.pseudo = pseudo;
    }
    public int getMatches() {
        return matches;
    }

    public void setMatches(int matches) {
        this.matches = matches;
    }
    public int getVictories() {
        return victories;
    }

    public void setVictories(int victories) {
        this.victories = victories;
    }

    public gametournament_Tournament getGametournament_tournament() {
        return gametournament_tournament;
    }

    public void setGametournament_tournament(gametournament_Tournament gametournament_tournament) {
        this.gametournament_tournament = gametournament_tournament;
    }

}