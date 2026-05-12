





import java.util.List;
import java.util.ArrayList;

public class rating___review  {

    private String inventoryID;
    private String reviews;
    private int rating;
    private String name;
    private String retailerID;
    private int ID;



    public rating___review(
        String inventoryID,        String reviews,        int rating,        String name,        String retailerID,        int ID    ) {
        this.inventoryID = inventoryID;
        this.reviews = reviews;
        this.rating = rating;
        this.name = name;
        this.retailerID = retailerID;
        this.ID = ID;
    }


    public String getInventoryid() {
        return inventoryID;
    }

    public void setInventoryid(String inventoryID) {
        this.inventoryID = inventoryID;
    }
    public String getReviews() {
        return reviews;
    }

    public void setReviews(String reviews) {
        this.reviews = reviews;
    }
    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRetailerid() {
        return retailerID;
    }

    public void setRetailerid(String retailerID) {
        this.retailerID = retailerID;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }


}