





import java.util.List;
import java.util.ArrayList;

public class Rating  {

    private None type;
    private int value;





    private Comment comment;




    private User user;




    private Course course;


    public Rating(
        None type,        int value    ) {
        this.type = type;
        this.value = value;
    }


    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public Comment getComment() {
        return comment;
    }

    public void setComment(Comment comment) {
        this.comment = comment;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public Course getCourse() {
        return course;
    }

    public void setCourse(Course course) {
        this.course = course;
    }

}