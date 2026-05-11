





import java.util.List;
import java.util.ArrayList;

public class rental_Car extends RentalObject {

    private String licensePlate;



    public rental_Car(
        String licensePlate    ) {
        super(
        );
        this.licensePlate = licensePlate;
    }


    public String getLicenseplate() {
        return licensePlate;
    }

    public void setLicenseplate(String licensePlate) {
        this.licensePlate = licensePlate;
    }


}