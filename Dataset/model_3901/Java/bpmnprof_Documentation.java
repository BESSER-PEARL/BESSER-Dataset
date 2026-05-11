





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_Documentation extends BaseElement {

    private String text;
    private String textFormat;





    private bpmnprof_BaseElement bpmnprof_baseelement;


    public bpmnprof_Documentation(
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

    public bpmnprof_BaseElement getBpmnprof_baseelement() {
        return bpmnprof_baseelement;
    }

    public void setBpmnprof_baseelement(bpmnprof_BaseElement bpmnprof_baseelement) {
        this.bpmnprof_baseelement = bpmnprof_baseelement;
    }

}