





import java.util.List;
import java.util.ArrayList;

public class vendor  {

    private String bookdetails;
    private String supplybooks;
    private String paymentdetails;
    private String search;



    public vendor(
        String bookdetails,        String supplybooks,        String paymentdetails,        String search    ) {
        this.bookdetails = bookdetails;
        this.supplybooks = supplybooks;
        this.paymentdetails = paymentdetails;
        this.search = search;
    }


    public String getBookdetails() {
        return bookdetails;
    }

    public void setBookdetails(String bookdetails) {
        this.bookdetails = bookdetails;
    }
    public String getSupplybooks() {
        return supplybooks;
    }

    public void setSupplybooks(String supplybooks) {
        this.supplybooks = supplybooks;
    }
    public String getPaymentdetails() {
        return paymentdetails;
    }

    public void setPaymentdetails(String paymentdetails) {
        this.paymentdetails = paymentdetails;
    }
    public String getSearch() {
        return search;
    }

    public void setSearch(String search) {
        this.search = search;
    }


}