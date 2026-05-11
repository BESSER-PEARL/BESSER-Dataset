





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Documentation extends BaseElement {

    private String text;
    private String textFormat;
    private String mixed;



    public BPMN2Model_Documentation(
        String text,        String textFormat,        String mixed    ) {
        super(
        );
        this.text = text;
        this.textFormat = textFormat;
        this.mixed = mixed;
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
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }


}