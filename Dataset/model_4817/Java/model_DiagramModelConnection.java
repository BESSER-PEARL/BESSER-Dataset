





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelConnection extends Documentable, DiagramModelComponent, Properties, FontAttribute {

    private int lineWidth;
    private String text;
    private String lineColor;
    private int type;



    public model_DiagramModelConnection(
        int lineWidth,        String text,        String lineColor,        int type    ) {
        super(
        );
        this.lineWidth = lineWidth;
        this.text = text;
        this.lineColor = lineColor;
        this.type = type;
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
    public String getLinecolor() {
        return lineColor;
    }

    public void setLinecolor(String lineColor) {
        this.lineColor = lineColor;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }


}