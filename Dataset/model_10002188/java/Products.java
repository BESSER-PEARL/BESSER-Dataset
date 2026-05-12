





import java.util.List;
import java.util.ArrayList;

public class Products  {

    private int TypeID1;
    private int Index;
    private String DateCreate;
    private int TypeID;
    private int ProductID;
    private int InStock;
    private String ProductInfo;
    private int CollectionID;



    public Products(
        int TypeID1,        int Index,        String DateCreate,        int TypeID,        int ProductID,        int InStock,        String ProductInfo,        int CollectionID    ) {
        this.TypeID1 = TypeID1;
        this.Index = Index;
        this.DateCreate = DateCreate;
        this.TypeID = TypeID;
        this.ProductID = ProductID;
        this.InStock = InStock;
        this.ProductInfo = ProductInfo;
        this.CollectionID = CollectionID;
    }


    public int getTypeid1() {
        return TypeID1;
    }

    public void setTypeid1(int TypeID1) {
        this.TypeID1 = TypeID1;
    }
    public int getIndex() {
        return Index;
    }

    public void setIndex(int Index) {
        this.Index = Index;
    }
    public String getDatecreate() {
        return DateCreate;
    }

    public void setDatecreate(String DateCreate) {
        this.DateCreate = DateCreate;
    }
    public int getTypeid() {
        return TypeID;
    }

    public void setTypeid(int TypeID) {
        this.TypeID = TypeID;
    }
    public int getProductid() {
        return ProductID;
    }

    public void setProductid(int ProductID) {
        this.ProductID = ProductID;
    }
    public int getInstock() {
        return InStock;
    }

    public void setInstock(int InStock) {
        this.InStock = InStock;
    }
    public String getProductinfo() {
        return ProductInfo;
    }

    public void setProductinfo(String ProductInfo) {
        this.ProductInfo = ProductInfo;
    }
    public int getCollectionid() {
        return CollectionID;
    }

    public void setCollectionid(int CollectionID) {
        this.CollectionID = CollectionID;
    }


}