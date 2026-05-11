





import java.util.List;
import java.util.ArrayList;

public class universityextended_administration_Lecture extends Event {

    private String captions;





    private Course course;


    public universityextended_administration_Lecture(
        String captions    ) {
        super(
        );
        this.captions = captions;
    }


    public String getCaptions() {
        return captions;
    }

    public void setCaptions(String captions) {
        this.captions = captions;
    }

    public Course getCourse() {
        return course;
    }

    public void setCourse(Course course) {
        this.course = course;
    }

}