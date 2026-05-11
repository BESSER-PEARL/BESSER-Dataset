





import java.util.List;
import java.util.ArrayList;

public class webshop_builder_3k_model_Component  {

    private int yposition;
    private int width;
    private int xposition;
    private String alignment;
    private int height;
    private String name;





    private webshop_builder_3k_model_Page webshop_builder_3k_model_page;


    public webshop_builder_3k_model_Component(
        int yposition,        int width,        int xposition,        String alignment,        int height,        String name    ) {
        this.yposition = yposition;
        this.width = width;
        this.xposition = xposition;
        this.alignment = alignment;
        this.height = height;
        this.name = name;
    }


    public int getYposition() {
        return yposition;
    }

    public void setYposition(int yposition) {
        this.yposition = yposition;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getXposition() {
        return xposition;
    }

    public void setXposition(int xposition) {
        this.xposition = xposition;
    }
    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public webshop_builder_3k_model_Page getWebshop_builder_3k_model_page() {
        return webshop_builder_3k_model_page;
    }

    public void setWebshop_builder_3k_model_page(webshop_builder_3k_model_Page webshop_builder_3k_model_page) {
        this.webshop_builder_3k_model_page = webshop_builder_3k_model_page;
    }

}