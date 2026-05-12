





import java.util.List;
import java.util.ArrayList;

public class Comment  {

    private String text;
    private String subject;





    private Course course;




    private User user;




    private Section section;


    public Comment(
        String text,        String subject    ) {
        this.text = text;
        this.subject = subject;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    public Course getCourse() {
        return course;
    }

    public void setCourse(Course course) {
        this.course = course;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public Section getSection() {
        return section;
    }

    public void setSection(Section section) {
        this.section = section;
    }

}