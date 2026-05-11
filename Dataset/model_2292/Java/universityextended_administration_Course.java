




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class universityextended_administration_Course  {

    private LocalDate startOfCourse;
    private LocalDate endOfCourse;
    private String title;





    private Lecture lecture;




    private Tutorial tutorial;


    public universityextended_administration_Course(
        LocalDate startOfCourse,        LocalDate endOfCourse,        String title    ) {
        this.startOfCourse = startOfCourse;
        this.endOfCourse = endOfCourse;
        this.title = title;
    }


    public LocalDate getStartofcourse() {
        return startOfCourse;
    }

    public void setStartofcourse(LocalDate startOfCourse) {
        this.startOfCourse = startOfCourse;
    }
    public LocalDate getEndofcourse() {
        return endOfCourse;
    }

    public void setEndofcourse(LocalDate endOfCourse) {
        this.endOfCourse = endOfCourse;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Lecture getLecture() {
        return lecture;
    }

    public void setLecture(Lecture lecture) {
        this.lecture = lecture;
    }
    public Tutorial getTutorial() {
        return tutorial;
    }

    public void setTutorial(Tutorial tutorial) {
        this.tutorial = tutorial;
    }

}