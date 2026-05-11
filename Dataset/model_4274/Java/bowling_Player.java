




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Player  {

    private int numberOfVictories;
    private String gender;
    private String winLossRatio;
    private LocalDate dateOfBirth;
    private String eMails;
    private String name;
    private float height;
    private boolean isProfessional;
    private String playedTournamentTypes;





    private bowling_Tournament bowling_tournament;


    public bowling_Player(
        int numberOfVictories,        String gender,        String winLossRatio,        LocalDate dateOfBirth,        String eMails,        String name,        float height,        boolean isProfessional,        String playedTournamentTypes    ) {
        this.numberOfVictories = numberOfVictories;
        this.gender = gender;
        this.winLossRatio = winLossRatio;
        this.dateOfBirth = dateOfBirth;
        this.eMails = eMails;
        this.name = name;
        this.height = height;
        this.isProfessional = isProfessional;
        this.playedTournamentTypes = playedTournamentTypes;
    }


    public int getNumberofvictories() {
        return numberOfVictories;
    }

    public void setNumberofvictories(int numberOfVictories) {
        this.numberOfVictories = numberOfVictories;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getWinlossratio() {
        return winLossRatio;
    }

    public void setWinlossratio(String winLossRatio) {
        this.winLossRatio = winLossRatio;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getEmails() {
        return eMails;
    }

    public void setEmails(String eMails) {
        this.eMails = eMails;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public boolean getIsprofessional() {
        return isProfessional;
    }

    public void setIsprofessional(boolean isProfessional) {
        this.isProfessional = isProfessional;
    }
    public String getPlayedtournamenttypes() {
        return playedTournamentTypes;
    }

    public void setPlayedtournamenttypes(String playedTournamentTypes) {
        this.playedTournamentTypes = playedTournamentTypes;
    }

    public bowling_Tournament getBowling_tournament() {
        return bowling_tournament;
    }

    public void setBowling_tournament(bowling_Tournament bowling_tournament) {
        this.bowling_tournament = bowling_tournament;
    }

}