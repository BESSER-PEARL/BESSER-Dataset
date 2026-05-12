





import java.util.List;
import java.util.ArrayList;

public class Topic  {






    private List<Vote> votes;


    public Topic(
    ) {
        this.votes = new ArrayList<>();
    }

    public Topic(
        ArrayList<Vote> votes    ) {
        this.votes = votes;
    }


    public List<Vote> getVotes() {
        return votes;
    }

    public void addVote(Vote vote) {
        this.votes.add(vote);
    }

}