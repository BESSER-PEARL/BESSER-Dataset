





import java.util.List;
import java.util.ArrayList;

public class duties_manager  {

    private boolean make_attendence;





    private List<doctor> doctors;




    private List<clinical> clinicals;


    public duties_manager(
        boolean make_attendence    ) {
        this.make_attendence = make_attendence;
        this.doctors = new ArrayList<>();
        this.clinicals = new ArrayList<>();
    }

    public duties_manager(
        boolean make_attendence        ArrayList<doctor> doctors,        ArrayList<clinical> clinicals    ) {
        this.make_attendence = make_attendence;
        this.doctors = doctors;
        this.clinicals = clinicals;
    }

    public boolean getMake_attendence() {
        return make_attendence;
    }

    public void setMake_attendence(boolean make_attendence) {
        this.make_attendence = make_attendence;
    }

    public List<doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }
    public List<clinical> getClinicals() {
        return clinicals;
    }

    public void addClinical(Clinical clinical) {
        this.clinicals.add(clinical);
    }

}