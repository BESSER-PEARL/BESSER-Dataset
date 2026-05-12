





import java.util.List;
import java.util.ArrayList;

public class Diagnosis  {

    private String LIst_of_Medicine;
    private int Patient_Id;
    private String LIst_of_Medical_Test;
    private String LIst_of_Instructions;
    private String Date;
    private String LIst_of_Diagnosis;
    private int ID;
    private String Condition;
    private String LIst_of_Symptoms;
    private int Doctor_Id;



    public Diagnosis(
        String LIst_of_Medicine,        int Patient_Id,        String LIst_of_Medical_Test,        String LIst_of_Instructions,        String Date,        String LIst_of_Diagnosis,        int ID,        String Condition,        String LIst_of_Symptoms,        int Doctor_Id    ) {
        this.LIst_of_Medicine = LIst_of_Medicine;
        this.Patient_Id = Patient_Id;
        this.LIst_of_Medical_Test = LIst_of_Medical_Test;
        this.LIst_of_Instructions = LIst_of_Instructions;
        this.Date = Date;
        this.LIst_of_Diagnosis = LIst_of_Diagnosis;
        this.ID = ID;
        this.Condition = Condition;
        this.LIst_of_Symptoms = LIst_of_Symptoms;
        this.Doctor_Id = Doctor_Id;
    }


    public String getList_of_medicine() {
        return LIst_of_Medicine;
    }

    public void setList_of_medicine(String LIst_of_Medicine) {
        this.LIst_of_Medicine = LIst_of_Medicine;
    }
    public int getPatient_id() {
        return Patient_Id;
    }

    public void setPatient_id(int Patient_Id) {
        this.Patient_Id = Patient_Id;
    }
    public String getList_of_medical_test() {
        return LIst_of_Medical_Test;
    }

    public void setList_of_medical_test(String LIst_of_Medical_Test) {
        this.LIst_of_Medical_Test = LIst_of_Medical_Test;
    }
    public String getList_of_instructions() {
        return LIst_of_Instructions;
    }

    public void setList_of_instructions(String LIst_of_Instructions) {
        this.LIst_of_Instructions = LIst_of_Instructions;
    }
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public String getList_of_diagnosis() {
        return LIst_of_Diagnosis;
    }

    public void setList_of_diagnosis(String LIst_of_Diagnosis) {
        this.LIst_of_Diagnosis = LIst_of_Diagnosis;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getCondition() {
        return Condition;
    }

    public void setCondition(String Condition) {
        this.Condition = Condition;
    }
    public String getList_of_symptoms() {
        return LIst_of_Symptoms;
    }

    public void setList_of_symptoms(String LIst_of_Symptoms) {
        this.LIst_of_Symptoms = LIst_of_Symptoms;
    }
    public int getDoctor_id() {
        return Doctor_Id;
    }

    public void setDoctor_id(int Doctor_Id) {
        this.Doctor_Id = Doctor_Id;
    }


}