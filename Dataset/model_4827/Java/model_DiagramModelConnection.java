





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelConnection extends FontAttribute, Connectable, LineObject, Properties, Documentable {

    private int type;
    private String text;
    private int textPosition;



    public model_DiagramModelConnection(
        int type,        String text,        int textPosition    ) {
        super(
        );
        this.type = type;
        this.text = text;
        this.textPosition = textPosition;
    }


    public int getType() {
        return type;
    }

    public void setType(int type) {
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


}