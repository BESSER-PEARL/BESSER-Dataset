





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Documentation extends BaseElement {

    private String textFormat;
    private String mixed;
    private String text;





    private bpmn2_BaseElement bpmn2_baseelement;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_Documentation(
        String textFormat,        String mixed,        String text    ) {
        super(
        );
        this.textFormat = textFormat;
        this.mixed = mixed;
        this.text = text;
    }


    public String getTextformat() {
        return textFormat;
    }

    public void setTextformat(String textFormat) {
        this.textFormat = textFormat;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public bpmn2_BaseElement getBpmn2_baseelement() {
        return bpmn2_baseelement;
    }

    public void setBpmn2_baseelement(bpmn2_BaseElement bpmn2_baseelement) {
        this.bpmn2_baseelement = bpmn2_baseelement;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}