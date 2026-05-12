





import java.util.List;
import java.util.ArrayList;

public class Hospital__Receptionist  {

    private int Employee_ID;
    private String Name;





    private List<Hospital_Patients> hospital_patientss;


    public Hospital__Receptionist(
        int Employee_ID,        String Name    ) {
        this.Employee_ID = Employee_ID;
        this.Name = Name;
        this.hospital_patientss = new ArrayList<>();
    }

    public Hospital__Receptionist(
        int Employee_ID,        String Name        ArrayList<Hospital_Patients> hospital_patientss    ) {
        this.Employee_ID = Employee_ID;
        this.Name = Name;
        this.hospital_patientss = hospital_patientss;
    }

    public int getEmployee_id() {
        return Employee_ID;
    }

    public void setEmployee_id(int Employee_ID) {
        this.Employee_ID = Employee_ID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<Hospital_Patients> getHospital_patientss() {
        return hospital_patientss;
    }

    public void addHospital_patients(Hospital_patients hospital_patients) {
        this.hospital_patientss.add(hospital_patients);
    }

}