





import java.util.List;
import java.util.ArrayList;

public class Treatment  {

    private int procedureID;
    private int idTreatment;
    private int patientID;
    private int idBill;





    private Patient patient;


    public Treatment(
        int procedureID,        int idTreatment,        int patientID,        int idBill    ) {
        this.procedureID = procedureID;
        this.idTreatment = idTreatment;
        this.patientID = patientID;
        this.idBill = idBill;
    }


    public int getProcedureid() {
        return procedureID;
    }

    public void setProcedureid(int procedureID) {
        this.procedureID = procedureID;
    }
    public int getIdtreatment() {
        return idTreatment;
    }

    public void setIdtreatment(int idTreatment) {
        this.idTreatment = idTreatment;
    }
    public int getPatientid() {
        return patientID;
    }

    public void setPatientid(int patientID) {
        this.patientID = patientID;
    }
    public int getIdbill() {
        return idBill;
    }

    public void setIdbill(int idBill) {
        this.idBill = idBill;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}