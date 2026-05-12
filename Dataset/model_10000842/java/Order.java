




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String cardDetails;
    private int transactionID;
    private LocalDate purchaseDate;
    private String productDetails;





    private Retailer retailer;




    private Farmer farmer;


    public Order(
        String cardDetails,        int transactionID,        LocalDate purchaseDate,        String productDetails    ) {
        this.cardDetails = cardDetails;
        this.transactionID = transactionID;
        this.purchaseDate = purchaseDate;
        this.productDetails = productDetails;
    }


    public String getCarddetails() {
        return cardDetails;
    }

    public void setCarddetails(String cardDetails) {
        this.cardDetails = cardDetails;
    }
    public int getTransactionid() {
        return transactionID;
    }

    public void setTransactionid(int transactionID) {
        this.transactionID = transactionID;
    }
    public LocalDate getPurchasedate() {
        return purchaseDate;
    }

    public void setPurchasedate(LocalDate purchaseDate) {
        this.purchaseDate = purchaseDate;
    }
    public String getProductdetails() {
        return productDetails;
    }

    public void setProductdetails(String productDetails) {
        this.productDetails = productDetails;
    }

    public Retailer getRetailer() {
        return retailer;
    }

    public void setRetailer(Retailer retailer) {
        this.retailer = retailer;
    }
    public Farmer getFarmer() {
        return farmer;
    }

    public void setFarmer(Farmer farmer) {
        this.farmer = farmer;
    }

}