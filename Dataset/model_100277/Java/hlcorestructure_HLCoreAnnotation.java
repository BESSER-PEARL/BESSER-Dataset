





import java.util.List;
import java.util.ArrayList;

public class hlcorestructure_HLCoreAnnotation extends Annotation {

    private String text;



    public hlcorestructure_HLCoreAnnotation(
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