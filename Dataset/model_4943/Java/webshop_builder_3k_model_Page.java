





import java.util.List;
import java.util.ArrayList;

public class webshop_builder_3k_model_Page  {

    private String canvas_color;
    private int height;
    private String title;
    private int width;





    private List<webshop_builder_3k_model_Reuse_component> webshop_builder_3k_model_reuse_components;


    public webshop_builder_3k_model_Page(
        String canvas_color,        int height,        String title,        int width    ) {
        this.canvas_color = canvas_color;
        this.height = height;
        this.title = title;
        this.width = width;
        this.webshop_builder_3k_model_reuse_components = new ArrayList<>();
    }

    public webshop_builder_3k_model_Page(
        String canvas_color,        int height,        String title,        int width        ArrayList<webshop_builder_3k_model_Reuse_component> webshop_builder_3k_model_reuse_components    ) {
        this.canvas_color = canvas_color;
        this.height = height;
        this.title = title;
        this.width = width;
        this.webshop_builder_3k_model_reuse_components = webshop_builder_3k_model_reuse_components;
    }

    public String getCanvas_color() {
        return canvas_color;
    }

    public void setCanvas_color(String canvas_color) {
        this.canvas_color = canvas_color;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    public List<webshop_builder_3k_model_Reuse_component> getWebshop_builder_3k_model_reuse_components() {
        return webshop_builder_3k_model_reuse_components;
    }

    public void addWebshop_builder_3k_model_reuse_component(Webshop_builder_3k_model_reuse_component webshop_builder_3k_model_reuse_component) {
        this.webshop_builder_3k_model_reuse_components.add(webshop_builder_3k_model_reuse_component);
    }

}