





import java.util.List;
import java.util.ArrayList;

public class CarRental2_Customer extends Person {

    private String address;



    public CarRental2_Customer(
        String address    ) {
        super(
        );
        this.address = address;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}