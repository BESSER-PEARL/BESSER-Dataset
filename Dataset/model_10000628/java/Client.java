





import java.util.List;
import java.util.ArrayList;

public class Client  {

    private String Id;
    private None Bookings;
    private String Name;
    private String Loyalty_card;





    private List<Problem> problems;


    public Client(
        String Id,        None Bookings,        String Name,        String Loyalty_card    ) {
        this.Id = Id;
        this.Bookings = Bookings;
        this.Name = Name;
        this.Loyalty_card = Loyalty_card;
        this.problems = new ArrayList<>();
    }

    public Client(
        String Id,        None Bookings,        String Name,        String Loyalty_card        ArrayList<Problem> problems    ) {
        this.Id = Id;
        this.Bookings = Bookings;
        this.Name = Name;
        this.Loyalty_card = Loyalty_card;
        this.problems = problems;
    }

    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public None getBookings() {
        return Bookings;
    }

    public void setBookings(None Bookings) {
        this.Bookings = Bookings;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getLoyalty_card() {
        return Loyalty_card;
    }

    public void setLoyalty_card(String Loyalty_card) {
        this.Loyalty_card = Loyalty_card;
    }

    public List<Problem> getProblems() {
        return problems;
    }

    public void addProblem(Problem problem) {
        this.problems.add(problem);
    }

}