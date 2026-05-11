





import java.util.List;
import java.util.ArrayList;

public class smm_Annotation extends SmmElement {

    private String text;



    public smm_Annotation(
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