





import java.util.List;
import java.util.ArrayList;

public class bpmn2_TextAnnotation extends Artifact {

    private String text;
    private String textFormat;



    public bpmn2_TextAnnotation(
        String text,        String textFormat    ) {
        super(
        );
        this.text = text;
        this.textFormat = textFormat;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getTextformat() {
        return textFormat;
    }

    public void setTextformat(String textFormat) {
        this.textFormat = textFormat;
    }


}