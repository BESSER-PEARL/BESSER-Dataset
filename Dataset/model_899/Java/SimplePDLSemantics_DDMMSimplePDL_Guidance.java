





import java.util.List;
import java.util.ArrayList;

public class SimplePDLSemantics_DDMMSimplePDL_Guidance extends ProcessElement {

    private String text;



    public SimplePDLSemantics_DDMMSimplePDL_Guidance(
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