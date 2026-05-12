





import java.util.List;
import java.util.ArrayList;

public class Patient_Check_In_aPatient  {

    private int MRN_Number;
    private String Patient_s_Name;
    private String Symptoms;
    private int Phone_Number;





    private Patient_Check_In_aDoctor patient_check_in_adoctor;




    private Patient_Check_In__aReceptionist patient_check_in__areceptionist;


    public Patient_Check_In_aPatient(
        int MRN_Number,        String Patient_s_Name,        String Symptoms,        int Phone_Number    ) {
        this.MRN_Number = MRN_Number;
        this.Patient_s_Name = Patient_s_Name;
        this.Symptoms = Symptoms;
        this.Phone_Number = Phone_Number;
    }


    public int getMrn_number() {
        return MRN_Number;
    }

    public void setMrn_number(int MRN_Number) {
        this.MRN_Number = MRN_Number;
    }
    public String getPatient_s_name() {
        return Patient_s_Name;
    }

    public void setPatient_s_name(String Patient_s_Name) {
        this.Patient_s_Name = Patient_s_Name;
    }
    public String getSymptoms() {
        return Symptoms;
    }

    public void setSymptoms(String Symptoms) {
        this.Symptoms = Symptoms;
    }
    public int getPhone_number() {
        return Phone_Number;
    }

    public void setPhone_number(int Phone_Number) {
        this.Phone_Number = Phone_Number;
    }

    public Patient_Check_In_aDoctor getPatient_check_in_adoctor() {
        return patient_check_in_adoctor;
    }

    public void setPatient_check_in_adoctor(Patient_Check_In_aDoctor patient_check_in_adoctor) {
        this.patient_check_in_adoctor = patient_check_in_adoctor;
    }
    public Patient_Check_In__aReceptionist getPatient_check_in__areceptionist() {
        return patient_check_in__areceptionist;
    }

    public void setPatient_check_in__areceptionist(Patient_Check_In__aReceptionist patient_check_in__areceptionist) {
        this.patient_check_in__areceptionist = patient_check_in__areceptionist;
    }

}