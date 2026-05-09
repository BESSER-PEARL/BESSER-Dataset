





import java.util.List;
import java.util.ArrayList;

public class pDL1_Guidance extends ProcessElement {

    private String text;



    public pDL1_Guidance(
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