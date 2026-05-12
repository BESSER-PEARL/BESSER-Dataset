





import java.util.List;
import java.util.ArrayList;

public class HasilBidding  {






    private List<Bidding> biddings;




    private List<User> users;


    public HasilBidding(
    ) {
        this.biddings = new ArrayList<>();
        this.users = new ArrayList<>();
    }

    public HasilBidding(
        ArrayList<Bidding> biddings,        ArrayList<User> users    ) {
        this.biddings = biddings;
        this.users = users;
    }


    public List<Bidding> getBiddings() {
        return biddings;
    }

    public void addBidding(Bidding bidding) {
        this.biddings.add(bidding);
    }
    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}