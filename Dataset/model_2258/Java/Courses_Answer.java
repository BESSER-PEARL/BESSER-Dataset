





import java.util.List;
import java.util.ArrayList;

public class Courses_Answer  {

    private boolean pass_;
    private int id;
    private String text;





    private Courses_Person courses_person;




    private Courses_Assignment courses_assignment;


    public Courses_Answer(
        boolean pass_,        int id,        String text    ) {
        this.pass_ = pass_;
        this.id = id;
        this.text = text;
    }


    public boolean getPass_() {
        return pass_;
    }

    public void setPass_(boolean pass_) {
        this.pass_ = pass_;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public Courses_Person getCourses_person() {
        return courses_person;
    }

    public void setCourses_person(Courses_Person courses_person) {
        this.courses_person = courses_person;
    }
    public Courses_Assignment getCourses_assignment() {
        return courses_assignment;
    }

    public void setCourses_assignment(Courses_Assignment courses_assignment) {
        this.courses_assignment = courses_assignment;
    }

}