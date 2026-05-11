





import java.util.List;
import java.util.ArrayList;

public class model_CustomColor  {

    private int B;
    private int G;
    private String name;
    private int R;





    private model_Color model_color;




    private model_Colors model_colors;


    public model_CustomColor(
        int B,        int G,        String name,        int R    ) {
        this.B = B;
        this.G = G;
        this.name = name;
        this.R = R;
    }


    public int getB() {
        return B;
    }

    public void setB(int B) {
        this.B = B;
    }
    public int getG() {
        return G;
    }

    public void setG(int G) {
        this.G = G;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getR() {
        return R;
    }

    public void setR(int R) {
        this.R = R;
    }

    public model_Color getModel_color() {
        return model_color;
    }

    public void setModel_color(model_Color model_color) {
        this.model_color = model_color;
    }
    public model_Colors getModel_colors() {
        return model_colors;
    }

    public void setModel_colors(model_Colors model_colors) {
        this.model_colors = model_colors;
    }

}