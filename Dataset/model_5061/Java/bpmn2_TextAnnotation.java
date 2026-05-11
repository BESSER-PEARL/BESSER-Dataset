





import java.util.List;
import java.util.ArrayList;

public class bpmn2_TextAnnotation extends Artifact {

    private String textFormat;
    private String text;



    public bpmn2_TextAnnotation(
        String textFormat,        String text    ) {
        super(
        );
        this.textFormat = textFormat;
        this.text = text;
    }


    public String getTextformat() {
        return textFormat;
    }

    public void setTextformat(String textFormat) {
        this.textFormat = textFormat;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}