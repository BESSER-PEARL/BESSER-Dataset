





import java.util.List;
import java.util.ArrayList;

public class RandL_TransactionReport  {

    private String totalEarned;
    private String balance;
    private String number;
    private String name;
    private String totalBurned;





    private RandL_CustomerCard randl_customercard;




    private RandL_Container_RandL randl_container_randl;




    private RandL_TransactionReportLine randl_transactionreportline;




    private List<RandL_TransactionReportLine> randl_transactionreportlines;




    private RandL_Date randl_date;




    private RandL_Date randl_date;


    public RandL_TransactionReport(
        String totalEarned,        String balance,        String number,        String name,        String totalBurned    ) {
        this.totalEarned = totalEarned;
        this.balance = balance;
        this.number = number;
        this.name = name;
        this.totalBurned = totalBurned;
        this.randl_transactionreportlines = new ArrayList<>();
    }

    public RandL_TransactionReport(
        String totalEarned,        String balance,        String number,        String name,        String totalBurned        ArrayList<RandL_TransactionReportLine> randl_transactionreportlines    ) {
        this.totalEarned = totalEarned;
        this.balance = balance;
        this.number = number;
        this.name = name;
        this.totalBurned = totalBurned;
        this.randl_transactionreportlines = randl_transactionreportlines;
    }

    public String getTotalearned() {
        return totalEarned;
    }

    public void setTotalearned(String totalEarned) {
        this.totalEarned = totalEarned;
    }
    public String getBalance() {
        return balance;
    }

    public void setBalance(String balance) {
        this.balance = balance;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTotalburned() {
        return totalBurned;
    }

    public void setTotalburned(String totalBurned) {
        this.totalBurned = totalBurned;
    }

    public RandL_CustomerCard getRandl_customercard() {
        return randl_customercard;
    }

    public void setRandl_customercard(RandL_CustomerCard randl_customercard) {
        this.randl_customercard = randl_customercard;
    }
    public RandL_Container_RandL getRandl_container_randl() {
        return randl_container_randl;
    }

    public void setRandl_container_randl(RandL_Container_RandL randl_container_randl) {
        this.randl_container_randl = randl_container_randl;
    }
    public RandL_TransactionReportLine getRandl_transactionreportline() {
        return randl_transactionreportline;
    }

    public void setRandl_transactionreportline(RandL_TransactionReportLine randl_transactionreportline) {
        this.randl_transactionreportline = randl_transactionreportline;
    }
    public List<RandL_TransactionReportLine> getRandl_transactionreportlines() {
        return randl_transactionreportlines;
    }

    public void addRandl_transactionreportline(Randl_transactionreportline randl_transactionreportline) {
        this.randl_transactionreportlines.add(randl_transactionreportline);
    }
    public RandL_Date getRandl_date() {
        return randl_date;
    }

    public void setRandl_date(RandL_Date randl_date) {
        this.randl_date = randl_date;
    }
    public RandL_Date getRandl_date() {
        return randl_date;
    }

    public void setRandl_date(RandL_Date randl_date) {
        this.randl_date = randl_date;
    }

}