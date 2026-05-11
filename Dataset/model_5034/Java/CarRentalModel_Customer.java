





import java.util.List;
import java.util.ArrayList;

public class CarRentalModel_Customer  {

    private String lastname;
    private String surname;
    private String identifier;





    private CarRentalModel_CarRental carrentalmodel_carrental;


    public CarRentalModel_Customer(
        String lastname,        String surname,        String identifier    ) {
        this.lastname = lastname;
        this.surname = surname;
        this.identifier = identifier;
    }


    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public CarRentalModel_CarRental getCarrentalmodel_carrental() {
        return carrentalmodel_carrental;
    }

    public void setCarrentalmodel_carrental(CarRentalModel_CarRental carrentalmodel_carrental) {
        this.carrentalmodel_carrental = carrentalmodel_carrental;
    }

}