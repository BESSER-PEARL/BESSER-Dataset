





import java.util.List;
import java.util.ArrayList;

public class RandL_CustomerCard  {

    private String valid;
    private String printedName;
    private String color;





    private RandL_Customer randl_customer;




    private RandL_Transaction randl_transaction;




    private RandL_Membership randl_membership;




    private RandL_Date randl_date;




    private RandL_Membership randl_membership;




    private List<RandL_Transaction> randl_transactions;




    private RandL_Customer randl_customer;




    private RandL_Date randl_date;




    private RandL_ServiceLevel randl_servicelevel;




    private RandL_Container_RandL randl_container_randl;


    public RandL_CustomerCard(
        String valid,        String printedName,        String color    ) {
        this.valid = valid;
        this.printedName = printedName;
        this.color = color;
        this.randl_transactions = new ArrayList<>();
    }

    public RandL_CustomerCard(
        String valid,        String printedName,        String color        ArrayList<RandL_Transaction> randl_transactions    ) {
        this.valid = valid;
        this.printedName = printedName;
        this.color = color;
        this.randl_transactions = randl_transactions;
    }

    public String getValid() {
        return valid;
    }

    public void setValid(String valid) {
        this.valid = valid;
    }
    public String getPrintedname() {
        return printedName;
    }

    public void setPrintedname(String printedName) {
        this.printedName = printedName;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public RandL_Customer getRandl_customer() {
        return randl_customer;
    }

    public void setRandl_customer(RandL_Customer randl_customer) {
        this.randl_customer = randl_customer;
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
    public RandL_Date getRandl_date() {
        return randl_date;
    }

    public void setRandl_date(RandL_Date randl_date) {
        this.randl_date = randl_date;
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
    public RandL_Customer getRandl_customer() {
        return randl_customer;
    }

    public void setRandl_customer(RandL_Customer randl_customer) {
        this.randl_customer = randl_customer;
    }
    public RandL_Date getRandl_date() {
        return randl_date;
    }

    public void setRandl_date(RandL_Date randl_date) {
        this.randl_date = randl_date;
    }
    public RandL_ServiceLevel getRandl_servicelevel() {
        return randl_servicelevel;
    }

    public void setRandl_servicelevel(RandL_ServiceLevel randl_servicelevel) {
        this.randl_servicelevel = randl_servicelevel;
    }
    public RandL_Container_RandL getRandl_container_randl() {
        return randl_container_randl;
    }

    public void setRandl_container_randl(RandL_Container_RandL randl_container_randl) {
        this.randl_container_randl = randl_container_randl;
    }

}