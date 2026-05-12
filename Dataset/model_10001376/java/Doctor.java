





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String Location;
    private String Speciality;



    public Doctor(
        String Location,        String Speciality    ) {
        this.Location = Location;
        this.Speciality = Speciality;
    }


    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }
    public String getSpeciality() {
        return Speciality;
    }

    public void setSpeciality(String Speciality) {
        this.Speciality = Speciality;
    }


}