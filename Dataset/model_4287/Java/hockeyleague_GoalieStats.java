





import java.util.List;
import java.util.ArrayList;

public class hockeyleague_GoalieStats  {

    private int goals;
    private int points;
    private float goalsAgainstAverage;
    private int assists;
    private String year;
    private int minutesPlayedIn;
    private int wins;
    private int penaltyMinutes;
    private int ties;
    private int goalsAgainst;
    private int shutouts;
    private int emptyNetGoals;
    private int losses;
    private int saves;
    private int gamesPlayedIn;





    private hockeyleague_Goalie hockeyleague_goalie;




    private hockeyleague_Team hockeyleague_team;


    public hockeyleague_GoalieStats(
        int goals,        int points,        float goalsAgainstAverage,        int assists,        String year,        int minutesPlayedIn,        int wins,        int penaltyMinutes,        int ties,        int goalsAgainst,        int shutouts,        int emptyNetGoals,        int losses,        int saves,        int gamesPlayedIn    ) {
        this.goals = goals;
        this.points = points;
        this.goalsAgainstAverage = goalsAgainstAverage;
        this.assists = assists;
        this.year = year;
        this.minutesPlayedIn = minutesPlayedIn;
        this.wins = wins;
        this.penaltyMinutes = penaltyMinutes;
        this.ties = ties;
        this.goalsAgainst = goalsAgainst;
        this.shutouts = shutouts;
        this.emptyNetGoals = emptyNetGoals;
        this.losses = losses;
        this.saves = saves;
        this.gamesPlayedIn = gamesPlayedIn;
    }


    public int getGoals() {
        return goals;
    }

    public void setGoals(int goals) {
        this.goals = goals;
    }
    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }
    public float getGoalsagainstaverage() {
        return goalsAgainstAverage;
    }

    public void setGoalsagainstaverage(float goalsAgainstAverage) {
        this.goalsAgainstAverage = goalsAgainstAverage;
    }
    public int getAssists() {
        return assists;
    }

    public void setAssists(int assists) {
        this.assists = assists;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public int getMinutesplayedin() {
        return minutesPlayedIn;
    }

    public void setMinutesplayedin(int minutesPlayedIn) {
        this.minutesPlayedIn = minutesPlayedIn;
    }
    public int getWins() {
        return wins;
    }

    public void setWins(int wins) {
        this.wins = wins;
    }
    public int getPenaltyminutes() {
        return penaltyMinutes;
    }

    public void setPenaltyminutes(int penaltyMinutes) {
        this.penaltyMinutes = penaltyMinutes;
    }
    public int getTies() {
        return ties;
    }

    public void setTies(int ties) {
        this.ties = ties;
    }
    public int getGoalsagainst() {
        return goalsAgainst;
    }

    public void setGoalsagainst(int goalsAgainst) {
        this.goalsAgainst = goalsAgainst;
    }
    public int getShutouts() {
        return shutouts;
    }

    public void setShutouts(int shutouts) {
        this.shutouts = shutouts;
    }
    public int getEmptynetgoals() {
        return emptyNetGoals;
    }

    public void setEmptynetgoals(int emptyNetGoals) {
        this.emptyNetGoals = emptyNetGoals;
    }
    public int getLosses() {
        return losses;
    }

    public void setLosses(int losses) {
        this.losses = losses;
    }
    public int getSaves() {
        return saves;
    }

    public void setSaves(int saves) {
        this.saves = saves;
    }
    public int getGamesplayedin() {
        return gamesPlayedIn;
    }

    public void setGamesplayedin(int gamesPlayedIn) {
        this.gamesPlayedIn = gamesPlayedIn;
    }

    public hockeyleague_Goalie getHockeyleague_goalie() {
        return hockeyleague_goalie;
    }

    public void setHockeyleague_goalie(hockeyleague_Goalie hockeyleague_goalie) {
        this.hockeyleague_goalie = hockeyleague_goalie;
    }
    public hockeyleague_Team getHockeyleague_team() {
        return hockeyleague_team;
    }

    public void setHockeyleague_team(hockeyleague_Team hockeyleague_team) {
        this.hockeyleague_team = hockeyleague_team;
    }

}