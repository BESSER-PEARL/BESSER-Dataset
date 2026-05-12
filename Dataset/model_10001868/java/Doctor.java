





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String specialty;
    private String locations;



    public Doctor(
        String specialty,        String locations    ) {
        this.specialty = specialty;
        this.locations = locations;
    }


    public String getSpecialty() {
        return specialty;
    }

    public void setSpecialty(String specialty) {
        this.specialty = specialty;
    }
    public String getLocations() {
        return locations;
    }

    public void setLocations(String locations) {
        this.locations = locations;
    }


}