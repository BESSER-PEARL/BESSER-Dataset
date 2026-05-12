





import java.util.List;
import java.util.ArrayList;

public class Client  {

    private String Id;
    private String Name;
    private String Loyalty_card;
    private None Bookings;





    private List<Problem> problems;


    public Client(
        String Id,        String Name,        String Loyalty_card,        None Bookings    ) {
        this.Id = Id;
        this.Name = Name;
        this.Loyalty_card = Loyalty_card;
        this.Bookings = Bookings;
        this.problems = new ArrayList<>();
    }

    public Client(
        String Id,        String Name,        String Loyalty_card,        None Bookings        ArrayList<Problem> problems    ) {
        this.Id = Id;
        this.Name = Name;
        this.Loyalty_card = Loyalty_card;
        this.Bookings = Bookings;
        this.problems = problems;
    }

    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
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
    public None getBookings() {
        return Bookings;
    }

    public void setBookings(None Bookings) {
        this.Bookings = Bookings;
    }

    public List<Problem> getProblems() {
        return problems;
    }

    public void addProblem(Problem problem) {
        this.problems.add(problem);
    }

}