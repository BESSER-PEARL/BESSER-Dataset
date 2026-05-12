





import java.util.List;
import java.util.ArrayList;

public class Message  {

    private String reciver;
    private String sender;
    private String message;





    private Student student;


    public Message(
        String reciver,        String sender,        String message    ) {
        this.reciver = reciver;
        this.sender = sender;
        this.message = message;
    }


    public String getReciver() {
        return reciver;
    }

    public void setReciver(String reciver) {
        this.reciver = reciver;
    }
    public String getSender() {
        return sender;
    }

    public void setSender(String sender) {
        this.sender = sender;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }

}