




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Fan  {

    private boolean hasSeasonTicket;
    private String gender;
    private float moneySpentOnTickets;
    private String name;
    private String eMails;
    private int numberOfTournamentsVisited;
    private LocalDate dateOfBirth;





    private List<bowling_Tournament> bowling_tournaments;




    private bowling_Player bowling_player;


    public bowling_Fan(
        boolean hasSeasonTicket,        String gender,        float moneySpentOnTickets,        String name,        String eMails,        int numberOfTournamentsVisited,        LocalDate dateOfBirth    ) {
        this.hasSeasonTicket = hasSeasonTicket;
        this.gender = gender;
        this.moneySpentOnTickets = moneySpentOnTickets;
        this.name = name;
        this.eMails = eMails;
        this.numberOfTournamentsVisited = numberOfTournamentsVisited;
        this.dateOfBirth = dateOfBirth;
        this.bowling_tournaments = new ArrayList<>();
    }

    public bowling_Fan(
        boolean hasSeasonTicket,        String gender,        float moneySpentOnTickets,        String name,        String eMails,        int numberOfTournamentsVisited,        LocalDate dateOfBirth        ArrayList<bowling_Tournament> bowling_tournaments    ) {
        this.hasSeasonTicket = hasSeasonTicket;
        this.gender = gender;
        this.moneySpentOnTickets = moneySpentOnTickets;
        this.name = name;
        this.eMails = eMails;
        this.numberOfTournamentsVisited = numberOfTournamentsVisited;
        this.dateOfBirth = dateOfBirth;
        this.bowling_tournaments = bowling_tournaments;
    }

    public boolean getHasseasonticket() {
        return hasSeasonTicket;
    }

    public void setHasseasonticket(boolean hasSeasonTicket) {
        this.hasSeasonTicket = hasSeasonTicket;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public float getMoneyspentontickets() {
        return moneySpentOnTickets;
    }

    public void setMoneyspentontickets(float moneySpentOnTickets) {
        this.moneySpentOnTickets = moneySpentOnTickets;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmails() {
        return eMails;
    }

    public void setEmails(String eMails) {
        this.eMails = eMails;
    }
    public int getNumberoftournamentsvisited() {
        return numberOfTournamentsVisited;
    }

    public void setNumberoftournamentsvisited(int numberOfTournamentsVisited) {
        this.numberOfTournamentsVisited = numberOfTournamentsVisited;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public List<bowling_Tournament> getBowling_tournaments() {
        return bowling_tournaments;
    }

    public void addBowling_tournament(Bowling_tournament bowling_tournament) {
        this.bowling_tournaments.add(bowling_tournament);
    }
    public bowling_Player getBowling_player() {
        return bowling_player;
    }

    public void setBowling_player(bowling_Player bowling_player) {
        this.bowling_player = bowling_player;
    }

}