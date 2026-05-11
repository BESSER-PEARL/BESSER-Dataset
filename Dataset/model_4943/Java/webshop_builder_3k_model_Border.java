





import java.util.List;
import java.util.ArrayList;

public class webshop_builder_3k_model_Border  {

    private int thickness;
    private String color;





    private webshop_builder_3k_model_Style webshop_builder_3k_model_style;


    public webshop_builder_3k_model_Border(
        int thickness,        String color    ) {
        this.thickness = thickness;
        this.color = color;
    }


    public int getThickness() {
        return thickness;
    }

    public void setThickness(int thickness) {
        this.thickness = thickness;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public webshop_builder_3k_model_Style getWebshop_builder_3k_model_style() {
        return webshop_builder_3k_model_style;
    }

    public void setWebshop_builder_3k_model_style(webshop_builder_3k_model_Style webshop_builder_3k_model_style) {
        this.webshop_builder_3k_model_style = webshop_builder_3k_model_style;
    }

}