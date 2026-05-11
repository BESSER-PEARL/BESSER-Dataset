




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowlingTournament_Player  {

    private String name;
    private boolean isProfessional;
    private float height;
    private LocalDate dateOfBirth;





    private bowlingTournament_League bowlingtournament_league;


    public bowlingTournament_Player(
        String name,        boolean isProfessional,        float height,        LocalDate dateOfBirth    ) {
        this.name = name;
        this.isProfessional = isProfessional;
        this.height = height;
        this.dateOfBirth = dateOfBirth;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsprofessional() {
        return isProfessional;
    }

    public void setIsprofessional(boolean isProfessional) {
        this.isProfessional = isProfessional;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public bowlingTournament_League getBowlingtournament_league() {
        return bowlingtournament_league;
    }

    public void setBowlingtournament_league(bowlingTournament_League bowlingtournament_league) {
        this.bowlingtournament_league = bowlingtournament_league;
    }

}