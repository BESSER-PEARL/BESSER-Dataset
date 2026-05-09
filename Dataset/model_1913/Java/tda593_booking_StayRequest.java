




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class tda593_booking_StayRequest  {

    private LocalDate timeStamp;
    private String text;
    private int id;



    public tda593_booking_StayRequest(
        LocalDate timeStamp,        String text,        int id    ) {
        this.timeStamp = timeStamp;
        this.text = text;
        this.id = id;
    }


    public LocalDate getTimestamp() {
        return timeStamp;
    }

    public void setTimestamp(LocalDate timeStamp) {
        this.timeStamp = timeStamp;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}