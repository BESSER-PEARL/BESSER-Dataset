





import java.util.List;
import java.util.ArrayList;

public class font_Greeting  {

    private String name;





    private font_Model font_model;


    public font_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public font_Model getFont_model() {
        return font_model;
    }

    public void setFont_model(font_Model font_model) {
        this.font_model = font_model;
    }

}