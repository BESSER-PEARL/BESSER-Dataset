





import java.util.List;
import java.util.ArrayList;

public class sofiagraphics_Style  {

    private boolean filled;
    private float lineWidth;





    private sofiagraphics_Widget sofiagraphics_widget;


    public sofiagraphics_Style(
        boolean filled,        float lineWidth    ) {
        this.filled = filled;
        this.lineWidth = lineWidth;
    }


    public boolean getFilled() {
        return filled;
    }

    public void setFilled(boolean filled) {
        this.filled = filled;
    }
    public float getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(float lineWidth) {
        this.lineWidth = lineWidth;
    }

    public sofiagraphics_Widget getSofiagraphics_widget() {
        return sofiagraphics_widget;
    }

    public void setSofiagraphics_widget(sofiagraphics_Widget sofiagraphics_widget) {
        this.sofiagraphics_widget = sofiagraphics_widget;
    }

}