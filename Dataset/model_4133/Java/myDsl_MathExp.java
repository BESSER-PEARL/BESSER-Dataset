





import java.util.List;
import java.util.ArrayList;

public class myDsl_MathExp extends Instance {

    private String text;



    public myDsl_MathExp(
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