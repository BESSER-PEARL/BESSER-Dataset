





import java.util.List;
import java.util.ArrayList;

public class myDsl01_Button extends UIElement {

    private String text;
    private String kind;



    public myDsl01_Button(
        String text,        String kind    ) {
        super(
        );
        this.text = text;
        this.kind = kind;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}