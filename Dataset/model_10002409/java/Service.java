





import java.util.List;
import java.util.ArrayList;

public class Service  {

    private String name;
    private String basePrice;
    private String description;





    private Hotel hotel;


    public Service(
        String name,        String basePrice,        String description    ) {
        this.name = name;
        this.basePrice = basePrice;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBaseprice() {
        return basePrice;
    }

    public void setBaseprice(String basePrice) {
        this.basePrice = basePrice;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Hotel getHotel() {
        return hotel;
    }

    public void setHotel(Hotel hotel) {
        this.hotel = hotel;
    }

}