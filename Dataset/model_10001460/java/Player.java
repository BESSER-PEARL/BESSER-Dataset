





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String role;
    private None night_target;
    private None vote_for;
    private int votes;
    private boolean isAlive;



    public Player(
        String role,        None night_target,        None vote_for,        int votes,        boolean isAlive    ) {
        this.role = role;
        this.night_target = night_target;
        this.vote_for = vote_for;
        this.votes = votes;
        this.isAlive = isAlive;
    }


    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public None getNight_target() {
        return night_target;
    }

    public void setNight_target(None night_target) {
        this.night_target = night_target;
    }
    public None getVote_for() {
        return vote_for;
    }

    public void setVote_for(None vote_for) {
        this.vote_for = vote_for;
    }
    public int getVotes() {
        return votes;
    }

    public void setVotes(int votes) {
        this.votes = votes;
    }
    public boolean getIsalive() {
        return isAlive;
    }

    public void setIsalive(boolean isAlive) {
        this.isAlive = isAlive;
    }


}