





import java.util.List;
import java.util.ArrayList;

public class Key  {

    private String Value;
    private String Length;
    private int coordinat_y;
    private int id;





    private Reciever reciever;




    private Sender sender;




    private Post post;


    public Key(
        String Value,        String Length,        int coordinat_y,        int id    ) {
        this.Value = Value;
        this.Length = Length;
        this.coordinat_y = coordinat_y;
        this.id = id;
    }


    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getLength() {
        return Length;
    }

    public void setLength(String Length) {
        this.Length = Length;
    }
    public int getCoordinat_y() {
        return coordinat_y;
    }

    public void setCoordinat_y(int coordinat_y) {
        this.coordinat_y = coordinat_y;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Reciever getReciever() {
        return reciever;
    }

    public void setReciever(Reciever reciever) {
        this.reciever = reciever;
    }
    public Sender getSender() {
        return sender;
    }

    public void setSender(Sender sender) {
        this.sender = sender;
    }
    public Post getPost() {
        return post;
    }

    public void setPost(Post post) {
        this.post = post;
    }

}