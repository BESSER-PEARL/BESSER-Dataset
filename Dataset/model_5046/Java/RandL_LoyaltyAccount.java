





import java.util.List;
import java.util.ArrayList;

public class RandL_LoyaltyAccount  {

    private String number;
    private String totalPointsEarned;
    private String points;





    private RandL_Transaction randl_transaction;




    private RandL_Membership randl_membership;




    private List<RandL_Transaction> randl_transactions;




    private RandL_Membership randl_membership;




    private List<RandL_Service> randl_services;


    public RandL_LoyaltyAccount(
        String number,        String totalPointsEarned,        String points    ) {
        this.number = number;
        this.totalPointsEarned = totalPointsEarned;
        this.points = points;
        this.randl_transactions = new ArrayList<>();
        this.randl_services = new ArrayList<>();
    }

    public RandL_LoyaltyAccount(
        String number,        String totalPointsEarned,        String points        ArrayList<RandL_Transaction> randl_transactions,        ArrayList<RandL_Service> randl_services    ) {
        this.number = number;
        this.totalPointsEarned = totalPointsEarned;
        this.points = points;
        this.randl_transactions = randl_transactions;
        this.randl_services = randl_services;
    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getTotalpointsearned() {
        return totalPointsEarned;
    }

    public void setTotalpointsearned(String totalPointsEarned) {
        this.totalPointsEarned = totalPointsEarned;
    }
    public String getPoints() {
        return points;
    }

    public void setPoints(String points) {
        this.points = points;
    }

    public RandL_Transaction getRandl_transaction() {
        return randl_transaction;
    }

    public void setRandl_transaction(RandL_Transaction randl_transaction) {
        this.randl_transaction = randl_transaction;
    }
    public RandL_Membership getRandl_membership() {
        return randl_membership;
    }

    public void setRandl_membership(RandL_Membership randl_membership) {
        this.randl_membership = randl_membership;
    }
    public List<RandL_Transaction> getRandl_transactions() {
        return randl_transactions;
    }

    public void addRandl_transaction(Randl_transaction randl_transaction) {
        this.randl_transactions.add(randl_transaction);
    }
    public RandL_Membership getRandl_membership() {
        return randl_membership;
    }

    public void setRandl_membership(RandL_Membership randl_membership) {
        this.randl_membership = randl_membership;
    }
    public List<RandL_Service> getRandl_services() {
        return randl_services;
    }

    public void addRandl_service(Randl_service randl_service) {
        this.randl_services.add(randl_service);
    }

}