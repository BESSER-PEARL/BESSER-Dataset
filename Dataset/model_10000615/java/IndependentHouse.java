





import java.util.List;
import java.util.ArrayList;

public class IndependentHouse  {

    private String Bathroom;
    private String Price;
    private String Bedroom;
    private String Size;
    private String YardSpace;





    private Property property;


    public IndependentHouse(
        String Bathroom,        String Price,        String Bedroom,        String Size,        String YardSpace    ) {
        this.Bathroom = Bathroom;
        this.Price = Price;
        this.Bedroom = Bedroom;
        this.Size = Size;
        this.YardSpace = YardSpace;
    }


    public String getBathroom() {
        return Bathroom;
    }

    public void setBathroom(String Bathroom) {
        this.Bathroom = Bathroom;
    }
    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }
    public String getBedroom() {
        return Bedroom;
    }

    public void setBedroom(String Bedroom) {
        this.Bedroom = Bedroom;
    }
    public String getSize() {
        return Size;
    }

    public void setSize(String Size) {
        this.Size = Size;
    }
    public String getYardspace() {
        return YardSpace;
    }

    public void setYardspace(String YardSpace) {
        this.YardSpace = YardSpace;
    }

    public Property getProperty() {
        return property;
    }

    public void setProperty(Property property) {
        this.property = property;
    }

}