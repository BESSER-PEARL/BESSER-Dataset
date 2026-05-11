





import java.util.List;
import java.util.ArrayList;

public class model_ColorFeature extends Feature {

    private String type;





    private model_Color model_color;


    public model_ColorFeature(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public model_Color getModel_color() {
        return model_color;
    }

    public void setModel_color(model_Color model_color) {
        this.model_color = model_color;
    }

}