





import java.util.List;
import java.util.ArrayList;

public class Farmer_produces  {

    private int ID;
    private String productList;
    private int farmerID;



    public Farmer_produces(
        int ID,        String productList,        int farmerID    ) {
        this.ID = ID;
        this.productList = productList;
        this.farmerID = farmerID;
    }


    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getProductlist() {
        return productList;
    }

    public void setProductlist(String productList) {
        this.productList = productList;
    }
    public int getFarmerid() {
        return farmerID;
    }

    public void setFarmerid(int farmerID) {
        this.farmerID = farmerID;
    }


}