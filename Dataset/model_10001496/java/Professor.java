





import java.util.List;
import java.util.ArrayList;

public class Professor  {

    private String attribute2;
    private int Lohn;



    public Professor(
        String attribute2,        int Lohn    ) {
        this.attribute2 = attribute2;
        this.Lohn = Lohn;
    }


    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public int getLohn() {
        return Lohn;
    }

    public void setLohn(int Lohn) {
        this.Lohn = Lohn;
    }


}