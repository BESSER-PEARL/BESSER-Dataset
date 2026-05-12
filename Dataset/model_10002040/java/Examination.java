





import java.util.List;
import java.util.ArrayList;

public class Examination  {

    private int no;
    private String attribute;
    private int Appointmentid;
    private int diagnosisid;





    private Appointment appointment;


    public Examination(
        int no,        String attribute,        int Appointmentid,        int diagnosisid    ) {
        this.no = no;
        this.attribute = attribute;
        this.Appointmentid = Appointmentid;
        this.diagnosisid = diagnosisid;
    }


    public int getNo() {
        return no;
    }

    public void setNo(int no) {
        this.no = no;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getAppointmentid() {
        return Appointmentid;
    }

    public void setAppointmentid(int Appointmentid) {
        this.Appointmentid = Appointmentid;
    }
    public int getDiagnosisid() {
        return diagnosisid;
    }

    public void setDiagnosisid(int diagnosisid) {
        this.diagnosisid = diagnosisid;
    }

    public Appointment getAppointment() {
        return appointment;
    }

    public void setAppointment(Appointment appointment) {
        this.appointment = appointment;
    }

}