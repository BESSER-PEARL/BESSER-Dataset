




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Player  {

    private String eMails;
    private LocalDate dateOfBirth;
    private String playedTournamentTypes;
    private String name;
    private String winLossRatio;
    private int numberOfVictories;
    private String gender;
    private float height;
    private boolean isProfessional;



    public bowling_Player(
        String eMails,        LocalDate dateOfBirth,        String playedTournamentTypes,        String name,        String winLossRatio,        int numberOfVictories,        String gender,        float height,        boolean isProfessional    ) {
        this.eMails = eMails;
        this.dateOfBirth = dateOfBirth;
        this.playedTournamentTypes = playedTournamentTypes;
        this.name = name;
        this.winLossRatio = winLossRatio;
        this.numberOfVictories = numberOfVictories;
        this.gender = gender;
        this.height = height;
        this.isProfessional = isProfessional;
    }


    public String getEmails() {
        return eMails;
    }

    public void setEmails(String eMails) {
        this.eMails = eMails;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getPlayedtournamenttypes() {
        return playedTournamentTypes;
    }

    public void setPlayedtournamenttypes(String playedTournamentTypes) {
        this.playedTournamentTypes = playedTournamentTypes;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getWinlossratio() {
        return winLossRatio;
    }

    public void setWinlossratio(String winLossRatio) {
        this.winLossRatio = winLossRatio;
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


}