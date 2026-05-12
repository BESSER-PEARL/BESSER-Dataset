





import java.util.List;
import java.util.ArrayList;

public class Hospital_Doctor  {

    private String Name;
    private String Rank;
    private int Salary;
    private String Specialization;
    private int ID;





    private List<Hospital_Patients> hospital_patientss;


    public Hospital_Doctor(
        String Name,        String Rank,        int Salary,        String Specialization,        int ID    ) {
        this.Name = Name;
        this.Rank = Rank;
        this.Salary = Salary;
        this.Specialization = Specialization;
        this.ID = ID;
        this.hospital_patientss = new ArrayList<>();
    }

    public Hospital_Doctor(
        String Name,        String Rank,        int Salary,        String Specialization,        int ID        ArrayList<Hospital_Patients> hospital_patientss    ) {
        this.Name = Name;
        this.Rank = Rank;
        this.Salary = Salary;
        this.Specialization = Specialization;
        this.ID = ID;
        this.hospital_patientss = hospital_patientss;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getRank() {
        return Rank;
    }

    public void setRank(String Rank) {
        this.Rank = Rank;
    }
    public int getSalary() {
        return Salary;
    }

    public void setSalary(int Salary) {
        this.Salary = Salary;
    }
    public String getSpecialization() {
        return Specialization;
    }

    public void setSpecialization(String Specialization) {
        this.Specialization = Specialization;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public List<Hospital_Patients> getHospital_patientss() {
        return hospital_patientss;
    }

    public void addHospital_patients(Hospital_patients hospital_patients) {
        this.hospital_patientss.add(hospital_patients);
    }

}