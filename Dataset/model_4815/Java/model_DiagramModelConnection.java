





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelConnection extends LineObject, DiagramModelComponent, Documentable, Properties, FontAttribute {

    private int type;
    private String text;



    public model_DiagramModelConnection(
        int type,        String text    ) {
        super(
        );
        this.type = type;
        this.text = text;
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


}