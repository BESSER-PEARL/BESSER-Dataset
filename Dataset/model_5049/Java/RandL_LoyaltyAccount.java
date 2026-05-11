





import java.util.List;
import java.util.ArrayList;

public class RandL_LoyaltyAccount  {

    private String number;
    private String points;
    private String totalPointsEarned;





    private RandL_Membership randl_membership;




    private RandL_Transaction randl_transaction;




    private List<RandL_Service> randl_services;




    private RandL_Membership randl_membership;




    private List<RandL_Transaction> randl_transactions;


    public RandL_LoyaltyAccount(
        String number,        String points,        String totalPointsEarned    ) {
        this.number = number;
        this.points = points;
        this.totalPointsEarned = totalPointsEarned;
        this.randl_services = new ArrayList<>();
        this.randl_transactions = new ArrayList<>();
    }

    public RandL_LoyaltyAccount(
        String number,        String points,        String totalPointsEarned        ArrayList<RandL_Service> randl_services,        ArrayList<RandL_Transaction> randl_transactions    ) {
        this.number = number;
        this.points = points;
        this.totalPointsEarned = totalPointsEarned;
        this.randl_services = randl_services;
        this.randl_transactions = randl_transactions;
    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getPoints() {
        return points;
    }

    public void setPoints(String points) {
        this.points = points;
    }
    public String getTotalpointsearned() {
        return totalPointsEarned;
    }

    public void setTotalpointsearned(String totalPointsEarned) {
        this.totalPointsEarned = totalPointsEarned;
    }

    public RandL_Membership getRandl_membership() {
        return randl_membership;
    }

    public void setRandl_membership(RandL_Membership randl_membership) {
        this.randl_membership = randl_membership;
    }
    public RandL_Transaction getRandl_transaction() {
        return randl_transaction;
    }

    public void setRandl_transaction(RandL_Transaction randl_transaction) {
        this.randl_transaction = randl_transaction;
    }
    public List<RandL_Service> getRandl_services() {
        return randl_services;
    }

    public void addRandl_service(Randl_service randl_service) {
        this.randl_services.add(randl_service);
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

}