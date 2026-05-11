





import java.util.List;
import java.util.ArrayList;

public class CarRental2_Customer extends Person {

    private int address;





    private CarRental2_Rental carrental2_rental;




    private List<CarRental2_Rental> carrental2_rentals;


    public CarRental2_Customer(
        int address    ) {
        super(
        );
        this.address = address;
        this.carrental2_rentals = new ArrayList<>();
    }

    public CarRental2_Customer(
        int address        ArrayList<CarRental2_Rental> carrental2_rentals    ) {
        this.address = address;
        this.carrental2_rentals = carrental2_rentals;
    }

    public int getAddress() {
        return address;
    }

    public void setAddress(int address) {
        this.address = address;
    }

    public CarRental2_Rental getCarrental2_rental() {
        return carrental2_rental;
    }

    public void setCarrental2_rental(CarRental2_Rental carrental2_rental) {
        this.carrental2_rental = carrental2_rental;
    }
    public List<CarRental2_Rental> getCarrental2_rentals() {
        return carrental2_rentals;
    }

    public void addCarrental2_rental(Carrental2_rental carrental2_rental) {
        this.carrental2_rentals.add(carrental2_rental);
    }

}