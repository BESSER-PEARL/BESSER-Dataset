





import java.util.List;
import java.util.ArrayList;

public class ward  {

    private String no_of_patients;
    private int ward_id;





    private Hospital hospital;


    public ward(
        String no_of_patients,        int ward_id    ) {
        this.no_of_patients = no_of_patients;
        this.ward_id = ward_id;
    }


    public String getNo_of_patients() {
        return no_of_patients;
    }

    public void setNo_of_patients(String no_of_patients) {
        this.no_of_patients = no_of_patients;
    }
    public int getWard_id() {
        return ward_id;
    }

    public void setWard_id(int ward_id) {
        this.ward_id = ward_id;
    }

    public Hospital getHospital() {
        return hospital;
    }

    public void setHospital(Hospital hospital) {
        this.hospital = hospital;
    }

}