





import java.util.List;
import java.util.ArrayList;

public class hockeyleague_GoalieStats  {

    private int saves;
    private int losses;
    private int minutesPlayedIn;
    private float goalsAgainstAverage;
    private int goalsAgainst;
    private int assists;
    private int wins;
    private int gamesPlayedIn;
    private int goals;
    private int points;
    private int emptyNetGoals;
    private int ties;
    private String year;
    private int penaltyMinutes;
    private int shutouts;





    private hockeyleague_Team hockeyleague_team;




    private hockeyleague_Goalie hockeyleague_goalie;


    public hockeyleague_GoalieStats(
        int saves,        int losses,        int minutesPlayedIn,        float goalsAgainstAverage,        int goalsAgainst,        int assists,        int wins,        int gamesPlayedIn,        int goals,        int points,        int emptyNetGoals,        int ties,        String year,        int penaltyMinutes,        int shutouts    ) {
        this.saves = saves;
        this.losses = losses;
        this.minutesPlayedIn = minutesPlayedIn;
        this.goalsAgainstAverage = goalsAgainstAverage;
        this.goalsAgainst = goalsAgainst;
        this.assists = assists;
        this.wins = wins;
        this.gamesPlayedIn = gamesPlayedIn;
        this.goals = goals;
        this.points = points;
        this.emptyNetGoals = emptyNetGoals;
        this.ties = ties;
        this.year = year;
        this.penaltyMinutes = penaltyMinutes;
        this.shutouts = shutouts;
    }


    public int getSaves() {
        return saves;
    }

    public void setSaves(int saves) {
        this.saves = saves;
    }
    public int getLosses() {
        return losses;
    }

    public void setLosses(int losses) {
        this.losses = losses;
    }
    public int getMinutesplayedin() {
        return minutesPlayedIn;
    }

    public void setMinutesplayedin(int minutesPlayedIn) {
        this.minutesPlayedIn = minutesPlayedIn;
    }
    public float getGoalsagainstaverage() {
        return goalsAgainstAverage;
    }

    public void setGoalsagainstaverage(float goalsAgainstAverage) {
        this.goalsAgainstAverage = goalsAgainstAverage;
    }
    public int getGoalsagainst() {
        return goalsAgainst;
    }

    public void setGoalsagainst(int goalsAgainst) {
        this.goalsAgainst = goalsAgainst;
    }
    public int getAssists() {
        return assists;
    }

    public void setAssists(int assists) {
        this.assists = assists;
    }
    public int getWins() {
        return wins;
    }

    public void setWins(int wins) {
        this.wins = wins;
    }
    public int getGamesplayedin() {
        return gamesPlayedIn;
    }

    public void setGamesplayedin(int gamesPlayedIn) {
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
    public int getEmptynetgoals() {
        return emptyNetGoals;
    }

    public void setEmptynetgoals(int emptyNetGoals) {
        this.emptyNetGoals = emptyNetGoals;
    }
    public int getTies() {
        return ties;
    }

    public void setTies(int ties) {
        this.ties = ties;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public int getPenaltyminutes() {
        return penaltyMinutes;
    }

    public void setPenaltyminutes(int penaltyMinutes) {
        this.penaltyMinutes = penaltyMinutes;
    }
    public int getShutouts() {
        return shutouts;
    }

    public void setShutouts(int shutouts) {
        this.shutouts = shutouts;
    }

    public hockeyleague_Team getHockeyleague_team() {
        return hockeyleague_team;
    }

    public void setHockeyleague_team(hockeyleague_Team hockeyleague_team) {
        this.hockeyleague_team = hockeyleague_team;
    }
    public hockeyleague_Goalie getHockeyleague_goalie() {
        return hockeyleague_goalie;
    }

    public void setHockeyleague_goalie(hockeyleague_Goalie hockeyleague_goalie) {
        this.hockeyleague_goalie = hockeyleague_goalie;
    }

}