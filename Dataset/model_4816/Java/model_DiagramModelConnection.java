





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelConnection extends FontAttribute, Properties, DiagramModelComponent, Documentable {

    private int lineWidth;
    private String text;
    private int type;
    private String lineColor;



    public model_DiagramModelConnection(
        int lineWidth,        String text,        int type,        String lineColor    ) {
        super(
        );
        this.lineWidth = lineWidth;
        this.text = text;
        this.type = type;
        this.lineColor = lineColor;
    }


    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getLinecolor() {
        return lineColor;
    }

    public void setLinecolor(String lineColor) {
        this.lineColor = lineColor;
    }


}