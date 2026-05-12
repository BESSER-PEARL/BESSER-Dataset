





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int cardId;
    private String fileName;
    private int ProductID;
    private String description;
    private String Price;
    private String Name;



    public Product(
        int cardId,        String fileName,        int ProductID,        String description,        String Price,        String Name    ) {
        this.cardId = cardId;
        this.fileName = fileName;
        this.ProductID = ProductID;
        this.description = description;
        this.Price = Price;
        this.Name = Name;
    }


    public int getCardid() {
        return cardId;
    }

    public void setCardid(int cardId) {
        this.cardId = cardId;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public int getProductid() {
        return ProductID;
    }

    public void setProductid(int ProductID) {
        this.ProductID = ProductID;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}