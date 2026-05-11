





import java.util.List;
import java.util.ArrayList;

public class sofiagraphics_Scene  {






    private List<sofiagraphics_Style> sofiagraphics_styles;




    private sofiagraphics_Widget sofiagraphics_widget;




    private List<sofiagraphics_Dimension> sofiagraphics_dimensions;




    private List<sofiagraphics_Point> sofiagraphics_points;




    private List<sofiagraphics_Widget> sofiagraphics_widgets;


    public sofiagraphics_Scene(
    ) {
        this.sofiagraphics_styles = new ArrayList<>();
        this.sofiagraphics_dimensions = new ArrayList<>();
        this.sofiagraphics_points = new ArrayList<>();
        this.sofiagraphics_widgets = new ArrayList<>();
    }

    public sofiagraphics_Scene(
        ArrayList<sofiagraphics_Style> sofiagraphics_styles,        ArrayList<sofiagraphics_Dimension> sofiagraphics_dimensions,        ArrayList<sofiagraphics_Point> sofiagraphics_points,        ArrayList<sofiagraphics_Widget> sofiagraphics_widgets    ) {
        this.sofiagraphics_styles = sofiagraphics_styles;
        this.sofiagraphics_dimensions = sofiagraphics_dimensions;
        this.sofiagraphics_points = sofiagraphics_points;
        this.sofiagraphics_widgets = sofiagraphics_widgets;
    }


    public List<sofiagraphics_Style> getSofiagraphics_styles() {
        return sofiagraphics_styles;
    }

    public void addSofiagraphics_style(Sofiagraphics_style sofiagraphics_style) {
        this.sofiagraphics_styles.add(sofiagraphics_style);
    }
    public sofiagraphics_Widget getSofiagraphics_widget() {
        return sofiagraphics_widget;
    }

    public void setSofiagraphics_widget(sofiagraphics_Widget sofiagraphics_widget) {
        this.sofiagraphics_widget = sofiagraphics_widget;
    }
    public List<sofiagraphics_Dimension> getSofiagraphics_dimensions() {
        return sofiagraphics_dimensions;
    }

    public void addSofiagraphics_dimension(Sofiagraphics_dimension sofiagraphics_dimension) {
        this.sofiagraphics_dimensions.add(sofiagraphics_dimension);
    }
    public List<sofiagraphics_Point> getSofiagraphics_points() {
        return sofiagraphics_points;
    }

    public void addSofiagraphics_point(Sofiagraphics_point sofiagraphics_point) {
        this.sofiagraphics_points.add(sofiagraphics_point);
    }
    public List<sofiagraphics_Widget> getSofiagraphics_widgets() {
        return sofiagraphics_widgets;
    }

    public void addSofiagraphics_widget(Sofiagraphics_widget sofiagraphics_widget) {
        this.sofiagraphics_widgets.add(sofiagraphics_widget);
    }

}