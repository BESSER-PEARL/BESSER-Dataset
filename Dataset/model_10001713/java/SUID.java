





import java.util.List;
import java.util.ArrayList;

public class SUID  {

    private String suFOODBal;
    private String studentName;
    private int ID;





    private Card card;


    public SUID(
        String suFOODBal,        String studentName,        int ID    ) {
        this.suFOODBal = suFOODBal;
        this.studentName = studentName;
        this.ID = ID;
    }


    public String getSufoodbal() {
        return suFOODBal;
    }

    public void setSufoodbal(String suFOODBal) {
        this.suFOODBal = suFOODBal;
    }
    public String getStudentname() {
        return studentName;
    }

    public void setStudentname(String studentName) {
        this.studentName = studentName;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public Card getCard() {
        return card;
    }

    public void setCard(Card card) {
        this.card = card;
    }

}