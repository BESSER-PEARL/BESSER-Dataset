





import java.util.List;
import java.util.ArrayList;

public class aredsl_NodeStyle  {

    private int width;
    private String semanticCondition;
    private int height;





    private aredsl_Node aredsl_node;


    public aredsl_NodeStyle(
        int width,        String semanticCondition,        int height    ) {
        this.width = width;
        this.semanticCondition = semanticCondition;
        this.height = height;
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
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    public aredsl_Node getAredsl_node() {
        return aredsl_node;
    }

    public void setAredsl_node(aredsl_Node aredsl_node) {
        this.aredsl_node = aredsl_node;
    }

}