





import java.util.List;
import java.util.ArrayList;

public class CarRental2_Customer extends Person {

    private int address;



    public CarRental2_Customer(
        int address    ) {
        super(
        );
        this.address = address;
    }


    public int getAddress() {
        return address;
    }

    public void setAddress(int address) {
        this.address = address;
    }


}