





import java.util.List;
import java.util.ArrayList;

public class gama_EChartLayer extends EGamaObject {

    private String value;
    private String color;
    private String style;



    public gama_EChartLayer(
        String value,        String color,        String style    ) {
        super(
        );
        this.value = value;
        this.color = color;
        this.style = style;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }


}