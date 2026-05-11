





import java.util.List;
import java.util.ArrayList;

public class sofiagraphics_Gesture  {






    private sofiagraphics_Scene sofiagraphics_scene;




    private List<sofiagraphics_Widget> sofiagraphics_widgets;


    public sofiagraphics_Gesture(
    ) {
        this.sofiagraphics_widgets = new ArrayList<>();
    }

    public sofiagraphics_Gesture(
        ArrayList<sofiagraphics_Widget> sofiagraphics_widgets    ) {
        this.sofiagraphics_widgets = sofiagraphics_widgets;
    }


    public sofiagraphics_Scene getSofiagraphics_scene() {
        return sofiagraphics_scene;
    }

    public void setSofiagraphics_scene(sofiagraphics_Scene sofiagraphics_scene) {
        this.sofiagraphics_scene = sofiagraphics_scene;
    }
    public List<sofiagraphics_Widget> getSofiagraphics_widgets() {
        return sofiagraphics_widgets;
    }

    public void addSofiagraphics_widget(Sofiagraphics_widget sofiagraphics_widget) {
        this.sofiagraphics_widgets.add(sofiagraphics_widget);
    }

}