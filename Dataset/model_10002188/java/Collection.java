





import java.util.List;
import java.util.ArrayList;

public class Collection  {

    private String CollectionName;
    private int CollectionID;





    private List<Products> productss;


    public Collection(
        String CollectionName,        int CollectionID    ) {
        this.CollectionName = CollectionName;
        this.CollectionID = CollectionID;
        this.productss = new ArrayList<>();
    }

    public Collection(
        String CollectionName,        int CollectionID        ArrayList<Products> productss    ) {
        this.CollectionName = CollectionName;
        this.CollectionID = CollectionID;
        this.productss = productss;
    }

    public String getCollectionname() {
        return CollectionName;
    }

    public void setCollectionname(String CollectionName) {
        this.CollectionName = CollectionName;
    }
    public int getCollectionid() {
        return CollectionID;
    }

    public void setCollectionid(int CollectionID) {
        this.CollectionID = CollectionID;
    }

    public List<Products> getProductss() {
        return productss;
    }

    public void addProducts(Products products) {
        this.productss.add(products);
    }

}