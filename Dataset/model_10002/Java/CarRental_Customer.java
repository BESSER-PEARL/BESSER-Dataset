





import java.util.List;
import java.util.ArrayList;

public class CarRental_Customer extends Person {

    private String address;





    private List<CarRental_Rental> carrental_rentals;




    private CarRental_Rental carrental_rental;


    public CarRental_Customer(
        String address    ) {
        super(
        );
        this.address = address;
        this.carrental_rentals = new ArrayList<>();
    }

    public CarRental_Customer(
        String address        ArrayList<CarRental_Rental> carrental_rentals    ) {
        this.address = address;
        this.carrental_rentals = carrental_rentals;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public List<CarRental_Rental> getCarrental_rentals() {
        return carrental_rentals;
    }

    public void addCarrental_rental(Carrental_rental carrental_rental) {
        this.carrental_rentals.add(carrental_rental);
    }
    public CarRental_Rental getCarrental_rental() {
        return carrental_rental;
    }

    public void setCarrental_rental(CarRental_Rental carrental_rental) {
        this.carrental_rental = carrental_rental;
    }

}