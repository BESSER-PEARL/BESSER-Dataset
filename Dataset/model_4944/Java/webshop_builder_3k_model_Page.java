





import java.util.List;
import java.util.ArrayList;

public class webshop_builder_3k_model_Page  {

    private String title;
    private int height;
    private int width;
    private String canvas_color;



    public webshop_builder_3k_model_Page(
        String title,        int height,        int width,        String canvas_color    ) {
        this.title = title;
        this.height = height;
        this.width = width;
        this.canvas_color = canvas_color;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public String getCanvas_color() {
        return canvas_color;
    }

    public void setCanvas_color(String canvas_color) {
        this.canvas_color = canvas_color;
    }


}