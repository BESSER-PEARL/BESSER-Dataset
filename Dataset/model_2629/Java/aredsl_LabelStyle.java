





import java.util.List;
import java.util.ArrayList;

public class aredsl_LabelStyle  {

    private String color;
    private String semanticCondition;
    private int height;





    private aredsl_Label aredsl_label;


    public aredsl_LabelStyle(
        String color,        String semanticCondition,        int height    ) {
        this.color = color;
        this.semanticCondition = semanticCondition;
        this.height = height;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
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

    public aredsl_Label getAredsl_label() {
        return aredsl_label;
    }

    public void setAredsl_label(aredsl_Label aredsl_label) {
        this.aredsl_label = aredsl_label;
    }

}