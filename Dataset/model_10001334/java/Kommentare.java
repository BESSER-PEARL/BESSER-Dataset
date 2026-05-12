





import java.util.List;
import java.util.ArrayList;

public class Kommentare  {

    private String text;





    private Beitrag beitrag;


    public Kommentare(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public Beitrag getBeitrag() {
        return beitrag;
    }

    public void setBeitrag(Beitrag beitrag) {
        this.beitrag = beitrag;
    }

}