





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String locations;
    private String specialty;



    public Doctor(
        String locations,        String specialty    ) {
        this.locations = locations;
        this.specialty = specialty;
    }


    public String getLocations() {
        return locations;
    }

    public void setLocations(String locations) {
        this.locations = locations;
    }
    public String getSpecialty() {
        return specialty;
    }

    public void setSpecialty(String specialty) {
        this.specialty = specialty;
    }


}