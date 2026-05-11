





import java.util.List;
import java.util.ArrayList;

public class flinkie2_Option  {

    private String text;





    private List<flinkie2_AssignStat> flinkie2_assignstats;




    private flinkie2_Question flinkie2_question;


    public flinkie2_Option(
        String text    ) {
        this.text = text;
        this.flinkie2_assignstats = new ArrayList<>();
    }

    public flinkie2_Option(
        String text        ArrayList<flinkie2_AssignStat> flinkie2_assignstats    ) {
        this.text = text;
        this.flinkie2_assignstats = flinkie2_assignstats;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public List<flinkie2_AssignStat> getFlinkie2_assignstats() {
        return flinkie2_assignstats;
    }

    public void addFlinkie2_assignstat(Flinkie2_assignstat flinkie2_assignstat) {
        this.flinkie2_assignstats.add(flinkie2_assignstat);
    }
    public flinkie2_Question getFlinkie2_question() {
        return flinkie2_question;
    }

    public void setFlinkie2_question(flinkie2_Question flinkie2_question) {
        this.flinkie2_question = flinkie2_question;
    }

}