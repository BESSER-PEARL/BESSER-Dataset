




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class e2_Lecture  {

    private LocalDate Date;
    private int Length;



    public e2_Lecture(
        LocalDate Date,        int Length    ) {
        this.Date = Date;
        this.Length = Length;
    }


    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }
    public int getLength() {
        return Length;
    }

    public void setLength(int Length) {
        this.Length = Length;
    }


}