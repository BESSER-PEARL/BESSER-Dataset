




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Game  {

    private LocalDate date;
    private int frames;





    private bowling_Matchup bowling_matchup;




    private bowling_Player bowling_player;




    private bowling_Matchup bowling_matchup;




    private bowling_Player bowling_player;


    public bowling_Game(
        LocalDate date,        int frames    ) {
        this.date = date;
        this.frames = frames;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public int getFrames() {
        return frames;
    }

    public void setFrames(int frames) {
        this.frames = frames;
    }

    public bowling_Matchup getBowling_matchup() {
        return bowling_matchup;
    }

    public void setBowling_matchup(bowling_Matchup bowling_matchup) {
        this.bowling_matchup = bowling_matchup;
    }
    public bowling_Player getBowling_player() {
        return bowling_player;
    }

    public void setBowling_player(bowling_Player bowling_player) {
        this.bowling_player = bowling_player;
    }
    public bowling_Matchup getBowling_matchup() {
        return bowling_matchup;
    }

    public void setBowling_matchup(bowling_Matchup bowling_matchup) {
        this.bowling_matchup = bowling_matchup;
    }
    public bowling_Player getBowling_player() {
        return bowling_player;
    }

    public void setBowling_player(bowling_Player bowling_player) {
        this.bowling_player = bowling_player;
    }

}