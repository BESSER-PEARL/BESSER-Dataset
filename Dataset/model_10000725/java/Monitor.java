




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Monitor  {

    private LocalDate Date;
    private int Time;
    private String Location;





    private Student student;


    public Monitor(
        LocalDate Date,        int Time,        String Location    ) {
        this.Date = Date;
        this.Time = Time;
        this.Location = Location;
    }


    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }
    public int getTime() {
        return Time;
    }

    public void setTime(int Time) {
        this.Time = Time;
    }
    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }

    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }

}