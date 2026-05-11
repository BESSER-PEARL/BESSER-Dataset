





import java.util.List;
import java.util.ArrayList;

public class CarRentalModel_Craft  {

    private String licenseNo;
    private float charge;
    private int vin;





    private CarRentalModel_CarRental carrentalmodel_carrental;


    public CarRentalModel_Craft(
        String licenseNo,        float charge,        int vin    ) {
        this.licenseNo = licenseNo;
        this.charge = charge;
        this.vin = vin;
    }


    public String getLicenseno() {
        return licenseNo;
    }

    public void setLicenseno(String licenseNo) {
        this.licenseNo = licenseNo;
    }
    public float getCharge() {
        return charge;
    }

    public void setCharge(float charge) {
        this.charge = charge;
    }
    public int getVin() {
        return vin;
    }

    public void setVin(int vin) {
        this.vin = vin;
    }

    public CarRentalModel_CarRental getCarrentalmodel_carrental() {
        return carrentalmodel_carrental;
    }

    public void setCarrentalmodel_carrental(CarRentalModel_CarRental carrentalmodel_carrental) {
        this.carrentalmodel_carrental = carrentalmodel_carrental;
    }

}