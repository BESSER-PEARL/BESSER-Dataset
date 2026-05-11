




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class e2_Lecture  {

    private LocalDate Date;
    private int Length;





    private List<e2_LectureContent> e2_lecturecontents;




    private e2_Course e2_course;


    public e2_Lecture(
        LocalDate Date,        int Length    ) {
        this.Date = Date;
        this.Length = Length;
        this.e2_lecturecontents = new ArrayList<>();
    }

    public e2_Lecture(
        LocalDate Date,        int Length        ArrayList<e2_LectureContent> e2_lecturecontents    ) {
        this.Date = Date;
        this.Length = Length;
        this.e2_lecturecontents = e2_lecturecontents;
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

    public List<e2_LectureContent> getE2_lecturecontents() {
        return e2_lecturecontents;
    }

    public void addE2_lecturecontent(E2_lecturecontent e2_lecturecontent) {
        this.e2_lecturecontents.add(e2_lecturecontent);
    }
    public e2_Course getE2_course() {
        return e2_course;
    }

    public void setE2_course(e2_Course e2_course) {
        this.e2_course = e2_course;
    }

}