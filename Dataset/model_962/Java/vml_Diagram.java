





import java.util.List;
import java.util.ArrayList;

public class vml_Diagram  {

    private String title;





    private vml_Model vml_model;


    public vml_Diagram(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public vml_Model getVml_model() {
        return vml_model;
    }

    public void setVml_model(vml_Model vml_model) {
        this.vml_model = vml_model;
    }

}