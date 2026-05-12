





import java.util.List;
import java.util.ArrayList;

public class Patients  {

    private String Patient_name;
    private String Sickness;
    private int Phone_no;
    private int NIC_NO;





    private Receptionist receptionist;




    private Docter docter;


    public Patients(
        String Patient_name,        String Sickness,        int Phone_no,        int NIC_NO    ) {
        this.Patient_name = Patient_name;
        this.Sickness = Sickness;
        this.Phone_no = Phone_no;
        this.NIC_NO = NIC_NO;
    }


    public String getPatient_name() {
        return Patient_name;
    }

    public void setPatient_name(String Patient_name) {
        this.Patient_name = Patient_name;
    }
    public String getSickness() {
        return Sickness;
    }

    public void setSickness(String Sickness) {
        this.Sickness = Sickness;
    }
    public int getPhone_no() {
        return Phone_no;
    }

    public void setPhone_no(int Phone_no) {
        this.Phone_no = Phone_no;
    }
    public int getNic_no() {
        return NIC_NO;
    }

    public void setNic_no(int NIC_NO) {
        this.NIC_NO = NIC_NO;
    }

    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }
    public Docter getDocter() {
        return docter;
    }

    public void setDocter(Docter docter) {
        this.docter = docter;
    }

}