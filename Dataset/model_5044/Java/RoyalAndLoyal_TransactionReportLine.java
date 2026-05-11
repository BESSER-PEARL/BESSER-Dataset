





import java.util.List;
import java.util.ArrayList;

public class RoyalAndLoyal_TransactionReportLine  {

    private String partnerName;
    private String serviceDesc;
    private int points;
    private float amount;





    private RoyalAndLoyal_Transaction royalandloyal_transaction;




    private RoyalAndLoyal_TransactionReport royalandloyal_transactionreport;




    private RoyalAndLoyal_TransactionReport royalandloyal_transactionreport;




    private RoyalAndLoyal_Date royalandloyal_date;


    public RoyalAndLoyal_TransactionReportLine(
        String partnerName,        String serviceDesc,        int points,        float amount    ) {
        this.partnerName = partnerName;
        this.serviceDesc = serviceDesc;
        this.points = points;
        this.amount = amount;
    }


    public String getPartnername() {
        return partnerName;
    }

    public void setPartnername(String partnerName) {
        this.partnerName = partnerName;
    }
    public String getServicedesc() {
        return serviceDesc;
    }

    public void setServicedesc(String serviceDesc) {
        this.serviceDesc = serviceDesc;
    }
    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }

    public RoyalAndLoyal_Transaction getRoyalandloyal_transaction() {
        return royalandloyal_transaction;
    }

    public void setRoyalandloyal_transaction(RoyalAndLoyal_Transaction royalandloyal_transaction) {
        this.royalandloyal_transaction = royalandloyal_transaction;
    }
    public RoyalAndLoyal_TransactionReport getRoyalandloyal_transactionreport() {
        return royalandloyal_transactionreport;
    }

    public void setRoyalandloyal_transactionreport(RoyalAndLoyal_TransactionReport royalandloyal_transactionreport) {
        this.royalandloyal_transactionreport = royalandloyal_transactionreport;
    }
    public RoyalAndLoyal_TransactionReport getRoyalandloyal_transactionreport() {
        return royalandloyal_transactionreport;
    }

    public void setRoyalandloyal_transactionreport(RoyalAndLoyal_TransactionReport royalandloyal_transactionreport) {
        this.royalandloyal_transactionreport = royalandloyal_transactionreport;
    }
    public RoyalAndLoyal_Date getRoyalandloyal_date() {
        return royalandloyal_date;
    }

    public void setRoyalandloyal_date(RoyalAndLoyal_Date royalandloyal_date) {
        this.royalandloyal_date = royalandloyal_date;
    }

}