




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class e2_Lecture  {

    private int length;
    private LocalDate Date;





    private e2_Course e2_course;


    public e2_Lecture(
        int length,        LocalDate Date    ) {
        this.length = length;
        this.Date = Date;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }

    public e2_Course getE2_course() {
        return e2_course;
    }

    public void setE2_course(e2_Course e2_course) {
        this.e2_course = e2_course;
    }

}