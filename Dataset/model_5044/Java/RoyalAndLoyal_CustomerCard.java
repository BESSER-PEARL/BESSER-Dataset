





import java.util.List;
import java.util.ArrayList;

public class RoyalAndLoyal_CustomerCard  {

    private String printedName;
    private boolean valid;
    private String color;





    private RoyalAndLoyal_Date royalandloyal_date;




    private RoyalAndLoyal_TransactionReport royalandloyal_transactionreport;




    private RoyalAndLoyal_Date royalandloyal_date;




    private RoyalAndLoyal_Transaction royalandloyal_transaction;




    private List<RoyalAndLoyal_Transaction> royalandloyal_transactions;




    private RoyalAndLoyal_Membership royalandloyal_membership;




    private RoyalAndLoyal_ServiceLevel royalandloyal_servicelevel;




    private RoyalAndLoyal_Membership royalandloyal_membership;


    public RoyalAndLoyal_CustomerCard(
        String printedName,        boolean valid,        String color    ) {
        this.printedName = printedName;
        this.valid = valid;
        this.color = color;
        this.royalandloyal_transactions = new ArrayList<>();
    }

    public RoyalAndLoyal_CustomerCard(
        String printedName,        boolean valid,        String color        ArrayList<RoyalAndLoyal_Transaction> royalandloyal_transactions    ) {
        this.printedName = printedName;
        this.valid = valid;
        this.color = color;
        this.royalandloyal_transactions = royalandloyal_transactions;
    }

    public String getPrintedname() {
        return printedName;
    }

    public void setPrintedname(String printedName) {
        this.printedName = printedName;
    }
    public boolean getValid() {
        return valid;
    }

    public void setValid(boolean valid) {
        this.valid = valid;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public RoyalAndLoyal_Date getRoyalandloyal_date() {
        return royalandloyal_date;
    }

    public void setRoyalandloyal_date(RoyalAndLoyal_Date royalandloyal_date) {
        this.royalandloyal_date = royalandloyal_date;
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
    public RoyalAndLoyal_Transaction getRoyalandloyal_transaction() {
        return royalandloyal_transaction;
    }

    public void setRoyalandloyal_transaction(RoyalAndLoyal_Transaction royalandloyal_transaction) {
        this.royalandloyal_transaction = royalandloyal_transaction;
    }
    public List<RoyalAndLoyal_Transaction> getRoyalandloyal_transactions() {
        return royalandloyal_transactions;
    }

    public void addRoyalandloyal_transaction(Royalandloyal_transaction royalandloyal_transaction) {
        this.royalandloyal_transactions.add(royalandloyal_transaction);
    }
    public RoyalAndLoyal_Membership getRoyalandloyal_membership() {
        return royalandloyal_membership;
    }

    public void setRoyalandloyal_membership(RoyalAndLoyal_Membership royalandloyal_membership) {
        this.royalandloyal_membership = royalandloyal_membership;
    }
    public RoyalAndLoyal_ServiceLevel getRoyalandloyal_servicelevel() {
        return royalandloyal_servicelevel;
    }

    public void setRoyalandloyal_servicelevel(RoyalAndLoyal_ServiceLevel royalandloyal_servicelevel) {
        this.royalandloyal_servicelevel = royalandloyal_servicelevel;
    }
    public RoyalAndLoyal_Membership getRoyalandloyal_membership() {
        return royalandloyal_membership;
    }

    public void setRoyalandloyal_membership(RoyalAndLoyal_Membership royalandloyal_membership) {
        this.royalandloyal_membership = royalandloyal_membership;
    }

}