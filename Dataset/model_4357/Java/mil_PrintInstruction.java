





import java.util.List;
import java.util.ArrayList;

public class mil_PrintInstruction extends Instruction {

    private String text;



    public mil_PrintInstruction(
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