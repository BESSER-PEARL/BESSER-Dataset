





import java.util.List;
import java.util.ArrayList;

public class Hospital_Patients  {

    private String Patient_s_Name;
    private int NIC_Number;
    private int Phone_Number;
    private String Sickness;



    public Hospital_Patients(
        String Patient_s_Name,        int NIC_Number,        int Phone_Number,        String Sickness    ) {
        this.Patient_s_Name = Patient_s_Name;
        this.NIC_Number = NIC_Number;
        this.Phone_Number = Phone_Number;
        this.Sickness = Sickness;
    }


    public String getPatient_s_name() {
        return Patient_s_Name;
    }

    public void setPatient_s_name(String Patient_s_Name) {
        this.Patient_s_Name = Patient_s_Name;
    }
    public int getNic_number() {
        return NIC_Number;
    }

    public void setNic_number(int NIC_Number) {
        this.NIC_Number = NIC_Number;
    }
    public int getPhone_number() {
        return Phone_Number;
    }

    public void setPhone_number(int Phone_Number) {
        this.Phone_Number = Phone_Number;
    }
    public String getSickness() {
        return Sickness;
    }

    public void setSickness(String Sickness) {
        this.Sickness = Sickness;
    }


}