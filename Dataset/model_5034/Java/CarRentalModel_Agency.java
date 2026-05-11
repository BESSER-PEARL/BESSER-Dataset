





import java.util.List;
import java.util.ArrayList;

public class CarRentalModel_Agency  {

    private String place;
    private String street;
    private int zip;





    private CarRentalModel_CarRental carrentalmodel_carrental;




    private CarRentalModel_CarRental carrentalmodel_carrental;


    public CarRentalModel_Agency(
        String place,        String street,        int zip    ) {
        this.place = place;
        this.street = street;
        this.zip = zip;
    }


    public String getPlace() {
        return place;
    }

    public void setPlace(String place) {
        this.place = place;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public int getZip() {
        return zip;
    }

    public void setZip(int zip) {
        this.zip = zip;
    }

    public CarRentalModel_CarRental getCarrentalmodel_carrental() {
        return carrentalmodel_carrental;
    }

    public void setCarrentalmodel_carrental(CarRentalModel_CarRental carrentalmodel_carrental) {
        this.carrentalmodel_carrental = carrentalmodel_carrental;
    }
    public CarRentalModel_CarRental getCarrentalmodel_carrental() {
        return carrentalmodel_carrental;
    }

    public void setCarrentalmodel_carrental(CarRentalModel_CarRental carrentalmodel_carrental) {
        this.carrentalmodel_carrental = carrentalmodel_carrental;
    }

}