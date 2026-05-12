





import java.util.List;
import java.util.ArrayList;

public class PNML_Label extends LocatedElement {

    private String text;



    public PNML_Label(
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


}