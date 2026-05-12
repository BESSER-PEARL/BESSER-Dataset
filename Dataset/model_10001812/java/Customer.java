





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String address;
    private int phoneno;
    private String email;
    private String customerName;
    private String shippinginfo;
    private boolean surveys;
    private String creditcardinfo;
    private boolean newsLettersub;





    private promotions promotions;


    public Customer(
        String address,        int phoneno,        String email,        String customerName,        String shippinginfo,        boolean surveys,        String creditcardinfo,        boolean newsLettersub    ) {
        this.address = address;
        this.phoneno = phoneno;
        this.email = email;
        this.customerName = customerName;
        this.shippinginfo = shippinginfo;
        this.surveys = surveys;
        this.creditcardinfo = creditcardinfo;
        this.newsLettersub = newsLettersub;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getPhoneno() {
        return phoneno;
    }

    public void setPhoneno(int phoneno) {
        this.phoneno = phoneno;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getCustomername() {
        return customerName;
    }

    public void setCustomername(String customerName) {
        this.customerName = customerName;
    }
    public String getShippinginfo() {
        return shippinginfo;
    }

    public void setShippinginfo(String shippinginfo) {
        this.shippinginfo = shippinginfo;
    }
    public boolean getSurveys() {
        return surveys;
    }

    public void setSurveys(boolean surveys) {
        this.surveys = surveys;
    }
    public String getCreditcardinfo() {
        return creditcardinfo;
    }

    public void setCreditcardinfo(String creditcardinfo) {
        this.creditcardinfo = creditcardinfo;
    }
    public boolean getNewslettersub() {
        return newsLettersub;
    }

    public void setNewslettersub(boolean newsLettersub) {
        this.newsLettersub = newsLettersub;
    }

    public promotions getPromotions() {
        return promotions;
    }

    public void setPromotions(promotions promotions) {
        this.promotions = promotions;
    }

}