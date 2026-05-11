




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Matchup  {

    private LocalDate date;





    private bowling_Tournament bowling_tournament;




    private bowling_Game bowling_game;




    private List<bowling_Game> bowling_games;


    public bowling_Matchup(
        LocalDate date    ) {
        this.date = date;
        this.bowling_games = new ArrayList<>();
    }

    public bowling_Matchup(
        LocalDate date        ArrayList<bowling_Game> bowling_games    ) {
        this.date = date;
        this.bowling_games = bowling_games;
    }

    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public bowling_Tournament getBowling_tournament() {
        return bowling_tournament;
    }

    public void setBowling_tournament(bowling_Tournament bowling_tournament) {
        this.bowling_tournament = bowling_tournament;
    }
    public bowling_Game getBowling_game() {
        return bowling_game;
    }

    public void setBowling_game(bowling_Game bowling_game) {
        this.bowling_game = bowling_game;
    }
    public List<bowling_Game> getBowling_games() {
        return bowling_games;
    }

    public void addBowling_game(Bowling_game bowling_game) {
        this.bowling_games.add(bowling_game);
    }

}