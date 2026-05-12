





import java.util.List;
import java.util.ArrayList;

public class outPatient  {

    private String outDate;
    private String inDate;
    private String roomNumber;



    public outPatient(
        String outDate,        String inDate,        String roomNumber    ) {
        this.outDate = outDate;
        this.inDate = inDate;
        this.roomNumber = roomNumber;
    }


    public String getOutdate() {
        return outDate;
    }

    public void setOutdate(String outDate) {
        this.outDate = outDate;
    }
    public String getIndate() {
        return inDate;
    }

    public void setIndate(String inDate) {
        this.inDate = inDate;
    }
    public String getRoomnumber() {
        return roomNumber;
    }

    public void setRoomnumber(String roomNumber) {
        this.roomNumber = roomNumber;
    }


}