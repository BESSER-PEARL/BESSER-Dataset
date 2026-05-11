




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Player  {

    private String name;
    private LocalDate dateOfBirth;
    private boolean isProfessional;
    private float height;





    private bowling_Game bowling_game;




    private bowling_League bowling_league;


    public bowling_Player(
        String name,        LocalDate dateOfBirth,        boolean isProfessional,        float height    ) {
        this.name = name;
        this.dateOfBirth = dateOfBirth;
        this.isProfessional = isProfessional;
        this.height = height;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
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

    public bowling_Game getBowling_game() {
        return bowling_game;
    }

    public void setBowling_game(bowling_Game bowling_game) {
        this.bowling_game = bowling_game;
    }
    public bowling_League getBowling_league() {
        return bowling_league;
    }

    public void setBowling_league(bowling_League bowling_league) {
        this.bowling_league = bowling_league;
    }

}