





import java.util.List;
import java.util.ArrayList;

public class webshop_builder_3k_model_Component  {

    private int height;
    private String alignment;
    private int yposition;
    private int xposition;
    private int width;
    private String name;





    private webshop_builder_3k_model_Page webshop_builder_3k_model_page;


    public webshop_builder_3k_model_Component(
        int height,        String alignment,        int yposition,        int xposition,        int width,        String name    ) {
        this.height = height;
        this.alignment = alignment;
        this.yposition = yposition;
        this.xposition = xposition;
        this.width = width;
        this.name = name;
    }


    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }
    public int getYposition() {
        return yposition;
    }

    public void setYposition(int yposition) {
        this.yposition = yposition;
    }
    public int getXposition() {
        return xposition;
    }

    public void setXposition(int xposition) {
        this.xposition = xposition;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
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