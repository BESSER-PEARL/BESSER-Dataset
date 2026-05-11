





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelConnection extends LineObject, Connectable, Properties, FontAttribute, Documentable {

    private String text;
    private int textPosition;
    private int type;



    public model_DiagramModelConnection(
        String text,        int textPosition,        int type    ) {
        super(
        );
        this.text = text;
        this.textPosition = textPosition;
        this.type = type;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public int getTextposition() {
        return textPosition;
    }

    public void setTextposition(int textPosition) {
        this.textPosition = textPosition;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }


}