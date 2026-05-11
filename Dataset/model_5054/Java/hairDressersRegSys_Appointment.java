




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class hairDressersRegSys_Appointment  {

    private LocalDate EndTime;
    private LocalDate StartTime;
    private LocalDate Date;



    public hairDressersRegSys_Appointment(
        LocalDate EndTime,        LocalDate StartTime,        LocalDate Date    ) {
        this.EndTime = EndTime;
        this.StartTime = StartTime;
        this.Date = Date;
    }


    public LocalDate getEndtime() {
        return EndTime;
    }

    public void setEndtime(LocalDate EndTime) {
        this.EndTime = EndTime;
    }
    public LocalDate getStarttime() {
        return StartTime;
    }

    public void setStarttime(LocalDate StartTime) {
        this.StartTime = StartTime;
    }
    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }


}