





import java.util.List;
import java.util.ArrayList;

public class Diagnosis  {

    private String LIst_of_Instructions;
    private int Patient_Id;
    private int ID;
    private String LIst_of_Medical_Test;
    private int Doctor_Id;
    private String Date;
    private String LIst_of_Diagnosis;
    private String LIst_of_Medicine;
    private String Condition;
    private String LIst_of_Symptoms;



    public Diagnosis(
        String LIst_of_Instructions,        int Patient_Id,        int ID,        String LIst_of_Medical_Test,        int Doctor_Id,        String Date,        String LIst_of_Diagnosis,        String LIst_of_Medicine,        String Condition,        String LIst_of_Symptoms    ) {
        this.LIst_of_Instructions = LIst_of_Instructions;
        this.Patient_Id = Patient_Id;
        this.ID = ID;
        this.LIst_of_Medical_Test = LIst_of_Medical_Test;
        this.Doctor_Id = Doctor_Id;
        this.Date = Date;
        this.LIst_of_Diagnosis = LIst_of_Diagnosis;
        this.LIst_of_Medicine = LIst_of_Medicine;
        this.Condition = Condition;
        this.LIst_of_Symptoms = LIst_of_Symptoms;
    }


    public String getList_of_instructions() {
        return LIst_of_Instructions;
    }

    public void setList_of_instructions(String LIst_of_Instructions) {
        this.LIst_of_Instructions = LIst_of_Instructions;
    }
    public int getPatient_id() {
        return Patient_Id;
    }

    public void setPatient_id(int Patient_Id) {
        this.Patient_Id = Patient_Id;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getList_of_medical_test() {
        return LIst_of_Medical_Test;
    }

    public void setList_of_medical_test(String LIst_of_Medical_Test) {
        this.LIst_of_Medical_Test = LIst_of_Medical_Test;
    }
    public int getDoctor_id() {
        return Doctor_Id;
    }

    public void setDoctor_id(int Doctor_Id) {
        this.Doctor_Id = Doctor_Id;
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
    public String getList_of_medicine() {
        return LIst_of_Medicine;
    }

    public void setList_of_medicine(String LIst_of_Medicine) {
        this.LIst_of_Medicine = LIst_of_Medicine;
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


}