





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_TextAnnotation extends BPMNArtifact {

    private String textFormat;
    private String text;





    private bpmnprof_Comment bpmnprof_comment;


    public bpmnprof_TextAnnotation(
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

    public bpmnprof_Comment getBpmnprof_comment() {
        return bpmnprof_comment;
    }

    public void setBpmnprof_comment(bpmnprof_Comment bpmnprof_comment) {
        this.bpmnprof_comment = bpmnprof_comment;
    }

}