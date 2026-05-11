





import java.util.List;
import java.util.ArrayList;

public class model_WidgetContainer  {






    private model_Widget model_widget;




    private model_Master model_master;




    private model_Master model_master;




    private List<model_Widget> model_widgets;


    public model_WidgetContainer(
    ) {
        this.model_widgets = new ArrayList<>();
    }

    public model_WidgetContainer(
        ArrayList<model_Widget> model_widgets    ) {
        this.model_widgets = model_widgets;
    }


    public model_Widget getModel_widget() {
        return model_widget;
    }

    public void setModel_widget(model_Widget model_widget) {
        this.model_widget = model_widget;
    }
    public model_Master getModel_master() {
        return model_master;
    }

    public void setModel_master(model_Master model_master) {
        this.model_master = model_master;
    }
    public model_Master getModel_master() {
        return model_master;
    }

    public void setModel_master(model_Master model_master) {
        this.model_master = model_master;
    }
    public List<model_Widget> getModel_widgets() {
        return model_widgets;
    }

    public void addModel_widget(Model_widget model_widget) {
        this.model_widgets.add(model_widget);
    }

}