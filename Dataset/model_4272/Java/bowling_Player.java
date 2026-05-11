




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Player  {

    private LocalDate dateOfBirth;
    private float height;
    private String name;
    private boolean isProfessional;





    private bowling_League bowling_league;




    private bowling_Game bowling_game;


    public bowling_Player(
        LocalDate dateOfBirth,        float height,        String name,        boolean isProfessional    ) {
        this.dateOfBirth = dateOfBirth;
        this.height = height;
        this.name = name;
        this.isProfessional = isProfessional;
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

    public bowling_League getBowling_league() {
        return bowling_league;
    }

    public void setBowling_league(bowling_League bowling_league) {
        this.bowling_league = bowling_league;
    }
    public bowling_Game getBowling_game() {
        return bowling_game;
    }

    public void setBowling_game(bowling_Game bowling_game) {
        this.bowling_game = bowling_game;
    }

}