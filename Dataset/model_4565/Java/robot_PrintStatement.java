





import java.util.List;
import java.util.ArrayList;

public class robot_PrintStatement extends Statement {

    private String text;



    public robot_PrintStatement(
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