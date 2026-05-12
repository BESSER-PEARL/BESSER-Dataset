





import java.util.List;
import java.util.ArrayList;

public class Service  {

    private String name;
    private String description;
    private String basePrice;





    private Hotel hotel;


    public Service(
        String name,        String description,        String basePrice    ) {
        this.name = name;
        this.description = description;
        this.basePrice = basePrice;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getBaseprice() {
        return basePrice;
    }

    public void setBaseprice(String basePrice) {
        this.basePrice = basePrice;
    }

    public Hotel getHotel() {
        return hotel;
    }

    public void setHotel(Hotel hotel) {
        this.hotel = hotel;
    }

}