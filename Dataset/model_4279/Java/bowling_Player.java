




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Player  {

    private LocalDate dateOfBirth;
    private String name;





    private bowling_Game bowling_game;


    public bowling_Player(
        LocalDate dateOfBirth,        String name    ) {
        this.dateOfBirth = dateOfBirth;
        this.name = name;
    }


    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bowling_Game getBowling_game() {
        return bowling_game;
    }

    public void setBowling_game(bowling_Game bowling_game) {
        this.bowling_game = bowling_game;
    }

}