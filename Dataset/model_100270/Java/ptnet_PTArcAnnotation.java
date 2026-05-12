





import java.util.List;
import java.util.ArrayList;

public class ptnet_PTArcAnnotation extends Annotation {

    private String text;



    public ptnet_PTArcAnnotation(
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