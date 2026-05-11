





import java.util.List;
import java.util.ArrayList;

public class webapp_Operation extends NamedElement {






    private webapp_Model webapp_model;




    private webapp_AbstractView webapp_abstractview;


    public webapp_Operation(
    ) {
        super(
        );
    }



    public webapp_Model getWebapp_model() {
        return webapp_model;
    }

    public void setWebapp_model(webapp_Model webapp_model) {
        this.webapp_model = webapp_model;
    }
    public webapp_AbstractView getWebapp_abstractview() {
        return webapp_abstractview;
    }

    public void setWebapp_abstractview(webapp_AbstractView webapp_abstractview) {
        this.webapp_abstractview = webapp_abstractview;
    }

}