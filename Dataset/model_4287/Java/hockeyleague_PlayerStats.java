





import java.util.List;
import java.util.ArrayList;

public class hockeyleague_PlayerStats  {

    private int shots;
    private float shotPercentage;
    private int plusMinus;
    private int powerPlayGoals;
    private int gamesPlayedIn;
    private int penaltyMinutes;
    private int assists;
    private int shortHandedGoals;
    private String year;
    private int gameWinningGoals;
    private int points;
    private int goals;





    private hockeyleague_Defence hockeyleague_defence;




    private hockeyleague_Forward hockeyleague_forward;




    private hockeyleague_Team hockeyleague_team;


    public hockeyleague_PlayerStats(
        int shots,        float shotPercentage,        int plusMinus,        int powerPlayGoals,        int gamesPlayedIn,        int penaltyMinutes,        int assists,        int shortHandedGoals,        String year,        int gameWinningGoals,        int points,        int goals    ) {
        this.shots = shots;
        this.shotPercentage = shotPercentage;
        this.plusMinus = plusMinus;
        this.powerPlayGoals = powerPlayGoals;
        this.gamesPlayedIn = gamesPlayedIn;
        this.penaltyMinutes = penaltyMinutes;
        this.assists = assists;
        this.shortHandedGoals = shortHandedGoals;
        this.year = year;
        this.gameWinningGoals = gameWinningGoals;
        this.points = points;
        this.goals = goals;
    }


    public int getShots() {
        return shots;
    }

    public void setShots(int shots) {
        this.shots = shots;
    }
    public float getShotpercentage() {
        return shotPercentage;
    }

    public void setShotpercentage(float shotPercentage) {
        this.shotPercentage = shotPercentage;
    }
    public int getPlusminus() {
        return plusMinus;
    }

    public void setPlusminus(int plusMinus) {
        this.plusMinus = plusMinus;
    }
    public int getPowerplaygoals() {
        return powerPlayGoals;
    }

    public void setPowerplaygoals(int powerPlayGoals) {
        this.powerPlayGoals = powerPlayGoals;
    }
    public int getGamesplayedin() {
        return gamesPlayedIn;
    }

    public void setGamesplayedin(int gamesPlayedIn) {
        this.gamesPlayedIn = gamesPlayedIn;
    }
    public int getPenaltyminutes() {
        return penaltyMinutes;
    }

    public void setPenaltyminutes(int penaltyMinutes) {
        this.penaltyMinutes = penaltyMinutes;
    }
    public int getAssists() {
        return assists;
    }

    public void setAssists(int assists) {
        this.assists = assists;
    }
    public int getShorthandedgoals() {
        return shortHandedGoals;
    }

    public void setShorthandedgoals(int shortHandedGoals) {
        this.shortHandedGoals = shortHandedGoals;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public int getGamewinninggoals() {
        return gameWinningGoals;
    }

    public void setGamewinninggoals(int gameWinningGoals) {
        this.gameWinningGoals = gameWinningGoals;
    }
    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }
    public int getGoals() {
        return goals;
    }

    public void setGoals(int goals) {
        this.goals = goals;
    }

    public hockeyleague_Defence getHockeyleague_defence() {
        return hockeyleague_defence;
    }

    public void setHockeyleague_defence(hockeyleague_Defence hockeyleague_defence) {
        this.hockeyleague_defence = hockeyleague_defence;
    }
    public hockeyleague_Forward getHockeyleague_forward() {
        return hockeyleague_forward;
    }

    public void setHockeyleague_forward(hockeyleague_Forward hockeyleague_forward) {
        this.hockeyleague_forward = hockeyleague_forward;
    }
    public hockeyleague_Team getHockeyleague_team() {
        return hockeyleague_team;
    }

    public void setHockeyleague_team(hockeyleague_Team hockeyleague_team) {
        this.hockeyleague_team = hockeyleague_team;
    }

}