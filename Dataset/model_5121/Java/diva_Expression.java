





import java.util.List;
import java.util.ArrayList;

public class diva_Expression extends DiVAModelElement {

    private String text;





    private diva_Term diva_term;


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

    public diva_Term getDiva_term() {
        return diva_term;
    }

    public void setDiva_term(diva_Term diva_term) {
        this.diva_term = diva_term;
    }

}