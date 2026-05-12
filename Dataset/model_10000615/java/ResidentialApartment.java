





import java.util.List;
import java.util.ArrayList;

public class ResidentialApartment  {

    private String Price;
    private String BEDROOMS;
    private String PARKING;
    private String Size;
    private String MAINTAINENCE;



    public ResidentialApartment(
        String Price,        String BEDROOMS,        String PARKING,        String Size,        String MAINTAINENCE    ) {
        this.Price = Price;
        this.BEDROOMS = BEDROOMS;
        this.PARKING = PARKING;
        this.Size = Size;
        this.MAINTAINENCE = MAINTAINENCE;
    }


    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }
    public String getBedrooms() {
        return BEDROOMS;
    }

    public void setBedrooms(String BEDROOMS) {
        this.BEDROOMS = BEDROOMS;
    }
    public String getParking() {
        return PARKING;
    }

    public void setParking(String PARKING) {
        this.PARKING = PARKING;
    }
    public String getSize() {
        return Size;
    }

    public void setSize(String Size) {
        this.Size = Size;
    }
    public String getMaintainence() {
        return MAINTAINENCE;
    }

    public void setMaintainence(String MAINTAINENCE) {
        this.MAINTAINENCE = MAINTAINENCE;
    }


}