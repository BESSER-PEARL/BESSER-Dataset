





import java.util.List;
import java.util.ArrayList;

public class NBVR_Logic_Proposition extends FormulationForm {

    private String text;





    private Proposition proposition;


    public NBVR_Logic_Proposition(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public Proposition getProposition() {
        return proposition;
    }

    public void setProposition(Proposition proposition) {
        this.proposition = proposition;
    }

}