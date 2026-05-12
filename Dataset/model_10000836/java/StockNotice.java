





import java.util.List;
import java.util.ArrayList;

public class StockNotice  {

    private String MatchedPrice;
    private String ProductID;
    private float ID;
    private String Source;
    private String ProductName;



    public StockNotice(
        String MatchedPrice,        String ProductID,        float ID,        String Source,        String ProductName    ) {
        this.MatchedPrice = MatchedPrice;
        this.ProductID = ProductID;
        this.ID = ID;
        this.Source = Source;
        this.ProductName = ProductName;
    }


    public String getMatchedprice() {
        return MatchedPrice;
    }

    public void setMatchedprice(String MatchedPrice) {
        this.MatchedPrice = MatchedPrice;
    }
    public String getProductid() {
        return ProductID;
    }

    public void setProductid(String ProductID) {
        this.ProductID = ProductID;
    }
    public float getId() {
        return ID;
    }

    public void setId(float ID) {
        this.ID = ID;
    }
    public String getSource() {
        return Source;
    }

    public void setSource(String Source) {
        this.Source = Source;
    }
    public String getProductname() {
        return ProductName;
    }

    public void setProductname(String ProductName) {
        this.ProductName = ProductName;
    }


}