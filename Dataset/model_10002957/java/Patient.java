





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private None next_of_kind;
    private None marital_status;
    private int num;
    private None local_doctor;





    private List<Medication> medications;




    private OutPatient outpatient;




    private WaitingList waitinglist;




    private List<Appointment> appointments;


    public Patient(
        None next_of_kind,        None marital_status,        int num,        None local_doctor    ) {
        this.next_of_kind = next_of_kind;
        this.marital_status = marital_status;
        this.num = num;
        this.local_doctor = local_doctor;
        this.medications = new ArrayList<>();
        this.appointments = new ArrayList<>();
    }

    public Patient(
        None next_of_kind,        None marital_status,        int num,        None local_doctor        ArrayList<Medication> medications,        ArrayList<Appointment> appointments    ) {
        this.next_of_kind = next_of_kind;
        this.marital_status = marital_status;
        this.num = num;
        this.local_doctor = local_doctor;
        this.medications = medications;
        this.appointments = appointments;
    }

    public None getNext_of_kind() {
        return next_of_kind;
    }

    public void setNext_of_kind(None next_of_kind) {
        this.next_of_kind = next_of_kind;
    }
    public None getMarital_status() {
        return marital_status;
    }

    public void setMarital_status(None marital_status) {
        this.marital_status = marital_status;
    }
    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }
    public None getLocal_doctor() {
        return local_doctor;
    }

    public void setLocal_doctor(None local_doctor) {
        this.local_doctor = local_doctor;
    }

    public List<Medication> getMedications() {
        return medications;
    }

    public void addMedication(Medication medication) {
        this.medications.add(medication);
    }
    public OutPatient getOutpatient() {
        return outpatient;
    }

    public void setOutpatient(OutPatient outpatient) {
        this.outpatient = outpatient;
    }
    public WaitingList getWaitinglist() {
        return waitinglist;
    }

    public void setWaitinglist(WaitingList waitinglist) {
        this.waitinglist = waitinglist;
    }
    public List<Appointment> getAppointments() {
        return appointments;
    }

    public void addAppointment(Appointment appointment) {
        this.appointments.add(appointment);
    }

}