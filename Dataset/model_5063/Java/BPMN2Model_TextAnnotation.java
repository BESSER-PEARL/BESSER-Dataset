





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_TextAnnotation extends Artifact {

    private String text;
    private String textFormat;



    public BPMN2Model_TextAnnotation(
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