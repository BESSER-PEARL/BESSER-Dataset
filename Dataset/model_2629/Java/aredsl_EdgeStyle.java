





import java.util.List;
import java.util.ArrayList;

public class aredsl_EdgeStyle  {

    private int width;
    private String semanticCondition;
    private String color;
    private String kind;





    private aredsl_Edge aredsl_edge;


    public aredsl_EdgeStyle(
        int width,        String semanticCondition,        String color,        String kind    ) {
        this.width = width;
        this.semanticCondition = semanticCondition;
        this.color = color;
        this.kind = kind;
    }


    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public String getSemanticcondition() {
        return semanticCondition;
    }

    public void setSemanticcondition(String semanticCondition) {
        this.semanticCondition = semanticCondition;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public aredsl_Edge getAredsl_edge() {
        return aredsl_edge;
    }

    public void setAredsl_edge(aredsl_Edge aredsl_edge) {
        this.aredsl_edge = aredsl_edge;
    }

}