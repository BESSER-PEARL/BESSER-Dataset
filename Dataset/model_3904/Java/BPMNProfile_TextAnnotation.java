





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_TextAnnotation extends BPMNArtifact {

    private String textFormat;
    private String text;





    private BPMNProfile_Comment bpmnprofile_comment;


    public BPMNProfile_TextAnnotation(
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

    public BPMNProfile_Comment getBpmnprofile_comment() {
        return bpmnprofile_comment;
    }

    public void setBpmnprofile_comment(BPMNProfile_Comment bpmnprofile_comment) {
        this.bpmnprofile_comment = bpmnprofile_comment;
    }

}