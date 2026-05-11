




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Player  {

    private LocalDate dateOfBirth;
    private float height;
    private boolean isProfessional;
    private String name;





    private bowling_League bowling_league;


    public bowling_Player(
        LocalDate dateOfBirth,        float height,        boolean isProfessional,        String name    ) {
        this.dateOfBirth = dateOfBirth;
        this.height = height;
        this.isProfessional = isProfessional;
        this.name = name;
    }


    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bowling_League getBowling_league() {
        return bowling_league;
    }

    public void setBowling_league(bowling_League bowling_league) {
        this.bowling_league = bowling_league;
    }

}