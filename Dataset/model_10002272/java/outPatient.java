





import java.util.List;
import java.util.ArrayList;

public class outPatient  {

    private String outDate;
    private String roomNumber;
    private String inDate;



    public outPatient(
        String outDate,        String roomNumber,        String inDate    ) {
        this.outDate = outDate;
        this.roomNumber = roomNumber;
        this.inDate = inDate;
    }


    public String getOutdate() {
        return outDate;
    }

    public void setOutdate(String outDate) {
        this.outDate = outDate;
    }
    public String getRoomnumber() {
        return roomNumber;
    }

    public void setRoomnumber(String roomNumber) {
        this.roomNumber = roomNumber;
    }
    public String getIndate() {
        return inDate;
    }

    public void setIndate(String inDate) {
        this.inDate = inDate;
    }


}