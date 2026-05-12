





import java.util.List;
import java.util.ArrayList;

public class Friend  {

    private boolean acceptornot;
    private String friend____;





    private Student student;


    public Friend(
        boolean acceptornot,        String friend____    ) {
        this.acceptornot = acceptornot;
        this.friend____ = friend____;
    }


    public boolean getAcceptornot() {
        return acceptornot;
    }

    public void setAcceptornot(boolean acceptornot) {
        this.acceptornot = acceptornot;
    }
    public String getFriend____() {
        return friend____;
    }

    public void setFriend____(String friend____) {
        this.friend____ = friend____;
    }

    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }

}