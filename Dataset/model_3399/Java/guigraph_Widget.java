





import java.util.List;
import java.util.ArrayList;

public class guigraph_Widget extends AbstractModelElement {

    private String image;





    private guigraph_Widget guigraph_widget;


    public guigraph_Widget(
        String image    ) {
        super(
        );
        this.image = image;
    }


    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public guigraph_Widget getGuigraph_widget() {
        return guigraph_widget;
    }

    public void setGuigraph_widget(guigraph_Widget guigraph_widget) {
        this.guigraph_widget = guigraph_widget;
    }

}