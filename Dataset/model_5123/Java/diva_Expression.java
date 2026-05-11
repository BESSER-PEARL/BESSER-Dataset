





import java.util.List;
import java.util.ArrayList;

public class diva_Expression extends DiVAModelElement {

    private String text;





    private diva_Invariant diva_invariant;


    public diva_Expression(
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

    public diva_Invariant getDiva_invariant() {
        return diva_invariant;
    }

    public void setDiva_invariant(diva_Invariant diva_invariant) {
        this.diva_invariant = diva_invariant;
    }

}