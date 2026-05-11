





import java.util.List;
import java.util.ArrayList;

public class di_Line extends Node {

    private String style;
    private int lineDash;
    private String sourceNode;
    private String targetNode;
    private int width;
    private int color;
    private String sourceAnchor;
    private String targetAnchor;





    private di_Container di_container;


    public di_Line(
        String style,        int lineDash,        String sourceNode,        String targetNode,        int width,        int color,        String sourceAnchor,        String targetAnchor    ) {
        super(
        );
        this.style = style;
        this.lineDash = lineDash;
        this.sourceNode = sourceNode;
        this.targetNode = targetNode;
        this.width = width;
        this.color = color;
        this.sourceAnchor = sourceAnchor;
        this.targetAnchor = targetAnchor;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public int getLinedash() {
        return lineDash;
    }

    public void setLinedash(int lineDash) {
        this.lineDash = lineDash;
    }
    public String getSourcenode() {
        return sourceNode;
    }

    public void setSourcenode(String sourceNode) {
        this.sourceNode = sourceNode;
    }
    public String getTargetnode() {
        return targetNode;
    }

    public void setTargetnode(String targetNode) {
        this.targetNode = targetNode;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getColor() {
        return color;
    }

    public void setColor(int color) {
        this.color = color;
    }
    public String getSourceanchor() {
        return sourceAnchor;
    }

    public void setSourceanchor(String sourceAnchor) {
        this.sourceAnchor = sourceAnchor;
    }
    public String getTargetanchor() {
        return targetAnchor;
    }

    public void setTargetanchor(String targetAnchor) {
        this.targetAnchor = targetAnchor;
    }

    public di_Container getDi_container() {
        return di_container;
    }

    public void setDi_container(di_Container di_container) {
        this.di_container = di_container;
    }

}