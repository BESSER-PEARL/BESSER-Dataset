





import java.util.List;
import java.util.ArrayList;

public class trace_Output extends Step {

    private String text;



    public trace_Output(
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