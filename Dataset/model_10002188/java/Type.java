





import java.util.List;
import java.util.ArrayList;

public class Type  {

    private String TypeName;
    private int TypeID;





    private List<Products> productss;


    public Type(
        String TypeName,        int TypeID    ) {
        this.TypeName = TypeName;
        this.TypeID = TypeID;
        this.productss = new ArrayList<>();
    }

    public Type(
        String TypeName,        int TypeID        ArrayList<Products> productss    ) {
        this.TypeName = TypeName;
        this.TypeID = TypeID;
        this.productss = productss;
    }

    public String getTypename() {
        return TypeName;
    }

    public void setTypename(String TypeName) {
        this.TypeName = TypeName;
    }
    public int getTypeid() {
        return TypeID;
    }

    public void setTypeid(int TypeID) {
        this.TypeID = TypeID;
    }

    public List<Products> getProductss() {
        return productss;
    }

    public void addProducts(Products products) {
        this.productss.add(products);
    }

}