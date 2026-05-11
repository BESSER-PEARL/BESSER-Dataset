





import java.util.List;
import java.util.ArrayList;

public class model_Ellipse extends ConnectableElement {

    private boolean circle;
    private boolean ellipse;



    public model_Ellipse(
        boolean circle,        boolean ellipse    ) {
        super(
        );
        this.circle = circle;
        this.ellipse = ellipse;
    }


    public boolean getCircle() {
        return circle;
    }

    public void setCircle(boolean circle) {
        this.circle = circle;
    }
    public boolean getEllipse() {
        return ellipse;
    }

    public void setEllipse(boolean ellipse) {
        this.ellipse = ellipse;
    }


}