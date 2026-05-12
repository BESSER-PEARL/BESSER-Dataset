





import java.util.List;
import java.util.ArrayList;

public class RandL_LoyaltyAccount  {

    private String points;
    private String totalPointsEarned;
    private String number;





    private RandL_Transaction randl_transaction;




    private List<RandL_Transaction> randl_transactions;


    public RandL_LoyaltyAccount(
        String points,        String totalPointsEarned,        String number    ) {
        this.points = points;
        this.totalPointsEarned = totalPointsEarned;
        this.number = number;
        this.randl_transactions = new ArrayList<>();
    }

    public RandL_LoyaltyAccount(
        String points,        String totalPointsEarned,        String number        ArrayList<RandL_Transaction> randl_transactions    ) {
        this.points = points;
        this.totalPointsEarned = totalPointsEarned;
        this.number = number;
        this.randl_transactions = randl_transactions;
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
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public RandL_Transaction getRandl_transaction() {
        return randl_transaction;
    }

    public void setRandl_transaction(RandL_Transaction randl_transaction) {
        this.randl_transaction = randl_transaction;
    }
    public List<RandL_Transaction> getRandl_transactions() {
        return randl_transactions;
    }

    public void addRandl_transaction(Randl_transaction randl_transaction) {
        this.randl_transactions.add(randl_transaction);
    }

}