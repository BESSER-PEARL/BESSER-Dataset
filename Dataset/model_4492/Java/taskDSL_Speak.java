





import java.util.List;
import java.util.ArrayList;

public class taskDSL_Speak extends Action {

    private String text;



    public taskDSL_Speak(
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