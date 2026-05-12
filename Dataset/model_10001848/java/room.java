





import java.util.List;
import java.util.ArrayList;

public class room  {

    private String room_no;





    private patient patient;


    public room(
        String room_no    ) {
        this.room_no = room_no;
    }


    public String getRoom_no() {
        return room_no;
    }

    public void setRoom_no(String room_no) {
        this.room_no = room_no;
    }

    public patient getPatient() {
        return patient;
    }

    public void setPatient(patient patient) {
        this.patient = patient;
    }

}