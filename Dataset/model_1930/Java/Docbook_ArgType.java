





import java.util.List;
import java.util.ArrayList;

public class Docbook_ArgType  {

    private String choice;
    private String rep;
    private String mixed;



    public Docbook_ArgType(
        String choice,        String rep,        String mixed    ) {
        this.choice = choice;
        this.rep = rep;
        this.mixed = mixed;
    }


    public String getChoice() {
        return choice;
    }

    public void setChoice(String choice) {
        this.choice = choice;
    }
    public String getRep() {
        return rep;
    }

    public void setRep(String rep) {
        this.rep = rep;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }


}