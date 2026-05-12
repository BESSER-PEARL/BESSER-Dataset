





import java.util.List;
import java.util.ArrayList;

public class Products  {

    private String description;
    private int ID;
    private String reviews;
    private int rating;
    private int discount;
    private float selling_price;
    private String name;
    private String farmerID;
    private String inventoryID;





    private Farmer farmer;


    public Products(
        String description,        int ID,        String reviews,        int rating,        int discount,        float selling_price,        String name,        String farmerID,        String inventoryID    ) {
        this.description = description;
        this.ID = ID;
        this.reviews = reviews;
        this.rating = rating;
        this.discount = discount;
        this.selling_price = selling_price;
        this.name = name;
        this.farmerID = farmerID;
        this.inventoryID = inventoryID;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
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
    public int getDiscount() {
        return discount;
    }

    public void setDiscount(int discount) {
        this.discount = discount;
    }
    public float getSelling_price() {
        return selling_price;
    }

    public void setSelling_price(float selling_price) {
        this.selling_price = selling_price;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFarmerid() {
        return farmerID;
    }

    public void setFarmerid(String farmerID) {
        this.farmerID = farmerID;
    }
    public String getInventoryid() {
        return inventoryID;
    }

    public void setInventoryid(String inventoryID) {
        this.inventoryID = inventoryID;
    }

    public Farmer getFarmer() {
        return farmer;
    }

    public void setFarmer(Farmer farmer) {
        this.farmer = farmer;
    }

}