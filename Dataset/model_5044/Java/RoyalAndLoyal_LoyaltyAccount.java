





import java.util.List;
import java.util.ArrayList;

public class RoyalAndLoyal_LoyaltyAccount  {

    private int number;
    private int points;
    private int totalPointsEarned;





    private RoyalAndLoyal_Membership royalandloyal_membership;




    private RoyalAndLoyal_Membership royalandloyal_membership;




    private List<RoyalAndLoyal_Transaction> royalandloyal_transactions;




    private List<RoyalAndLoyal_Service> royalandloyal_services;




    private RoyalAndLoyal_Transaction royalandloyal_transaction;


    public RoyalAndLoyal_LoyaltyAccount(
        int number,        int points,        int totalPointsEarned    ) {
        this.number = number;
        this.points = points;
        this.totalPointsEarned = totalPointsEarned;
        this.royalandloyal_transactions = new ArrayList<>();
        this.royalandloyal_services = new ArrayList<>();
    }

    public RoyalAndLoyal_LoyaltyAccount(
        int number,        int points,        int totalPointsEarned        ArrayList<RoyalAndLoyal_Transaction> royalandloyal_transactions,        ArrayList<RoyalAndLoyal_Service> royalandloyal_services    ) {
        this.number = number;
        this.points = points;
        this.totalPointsEarned = totalPointsEarned;
        this.royalandloyal_transactions = royalandloyal_transactions;
        this.royalandloyal_services = royalandloyal_services;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }
    public int getTotalpointsearned() {
        return totalPointsEarned;
    }

    public void setTotalpointsearned(int totalPointsEarned) {
        this.totalPointsEarned = totalPointsEarned;
    }

    public RoyalAndLoyal_Membership getRoyalandloyal_membership() {
        return royalandloyal_membership;
    }

    public void setRoyalandloyal_membership(RoyalAndLoyal_Membership royalandloyal_membership) {
        this.royalandloyal_membership = royalandloyal_membership;
    }
    public RoyalAndLoyal_Membership getRoyalandloyal_membership() {
        return royalandloyal_membership;
    }

    public void setRoyalandloyal_membership(RoyalAndLoyal_Membership royalandloyal_membership) {
        this.royalandloyal_membership = royalandloyal_membership;
    }
    public List<RoyalAndLoyal_Transaction> getRoyalandloyal_transactions() {
        return royalandloyal_transactions;
    }

    public void addRoyalandloyal_transaction(Royalandloyal_transaction royalandloyal_transaction) {
        this.royalandloyal_transactions.add(royalandloyal_transaction);
    }
    public List<RoyalAndLoyal_Service> getRoyalandloyal_services() {
        return royalandloyal_services;
    }

    public void addRoyalandloyal_service(Royalandloyal_service royalandloyal_service) {
        this.royalandloyal_services.add(royalandloyal_service);
    }
    public RoyalAndLoyal_Transaction getRoyalandloyal_transaction() {
        return royalandloyal_transaction;
    }

    public void setRoyalandloyal_transaction(RoyalAndLoyal_Transaction royalandloyal_transaction) {
        this.royalandloyal_transaction = royalandloyal_transaction;
    }

}