





import java.util.List;
import java.util.ArrayList;

public class problog_Comment extends Statement {

    private String text;



    public problog_Comment(
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