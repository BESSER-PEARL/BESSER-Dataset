





import java.util.List;
import java.util.ArrayList;

public class Department  {






    private List<Hospital> hospitals;


    public Department(
    ) {
        this.hospitals = new ArrayList<>();
    }

    public Department(
        ArrayList<Hospital> hospitals    ) {
        this.hospitals = hospitals;
    }


    public List<Hospital> getHospitals() {
        return hospitals;
    }

    public void addHospital(Hospital hospital) {
        this.hospitals.add(hospital);
    }

}