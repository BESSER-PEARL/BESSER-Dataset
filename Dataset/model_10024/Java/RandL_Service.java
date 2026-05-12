





import java.util.List;
import java.util.ArrayList;

public class RandL_Service  {

    private String serviceNr;
    private String pointsBurned;
    private String condition;
    private String pointsEarned;
    private String description;





    private RandL_LoyaltyAccount randl_loyaltyaccount;




    private List<RandL_Transaction> randl_transactions;




    private RandL_Transaction randl_transaction;




    private RandL_ServiceLevel randl_servicelevel;




    private RandL_ServiceLevel randl_servicelevel;


    public RandL_Service(
        String serviceNr,        String pointsBurned,        String condition,        String pointsEarned,        String description    ) {
        this.serviceNr = serviceNr;
        this.pointsBurned = pointsBurned;
        this.condition = condition;
        this.pointsEarned = pointsEarned;
        this.description = description;
        this.randl_transactions = new ArrayList<>();
    }

    public RandL_Service(
        String serviceNr,        String pointsBurned,        String condition,        String pointsEarned,        String description        ArrayList<RandL_Transaction> randl_transactions    ) {
        this.serviceNr = serviceNr;
        this.pointsBurned = pointsBurned;
        this.condition = condition;
        this.pointsEarned = pointsEarned;
        this.description = description;
        this.randl_transactions = randl_transactions;
    }

    public String getServicenr() {
        return serviceNr;
    }

    public void setServicenr(String serviceNr) {
        this.serviceNr = serviceNr;
    }
    public String getPointsburned() {
        return pointsBurned;
    }

    public void setPointsburned(String pointsBurned) {
        this.pointsBurned = pointsBurned;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }
    public String getPointsearned() {
        return pointsEarned;
    }

    public void setPointsearned(String pointsEarned) {
        this.pointsEarned = pointsEarned;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public RandL_LoyaltyAccount getRandl_loyaltyaccount() {
        return randl_loyaltyaccount;
    }

    public void setRandl_loyaltyaccount(RandL_LoyaltyAccount randl_loyaltyaccount) {
        this.randl_loyaltyaccount = randl_loyaltyaccount;
    }
    public List<RandL_Transaction> getRandl_transactions() {
        return randl_transactions;
    }

    public void addRandl_transaction(Randl_transaction randl_transaction) {
        this.randl_transactions.add(randl_transaction);
    }
    public RandL_Transaction getRandl_transaction() {
        return randl_transaction;
    }

    public void setRandl_transaction(RandL_Transaction randl_transaction) {
        this.randl_transaction = randl_transaction;
    }
    public RandL_ServiceLevel getRandl_servicelevel() {
        return randl_servicelevel;
    }

    public void setRandl_servicelevel(RandL_ServiceLevel randl_servicelevel) {
        this.randl_servicelevel = randl_servicelevel;
    }
    public RandL_ServiceLevel getRandl_servicelevel() {
        return randl_servicelevel;
    }

    public void setRandl_servicelevel(RandL_ServiceLevel randl_servicelevel) {
        this.randl_servicelevel = randl_servicelevel;
    }

}