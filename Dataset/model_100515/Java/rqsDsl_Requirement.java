





import java.util.List;
import java.util.ArrayList;

public class rqsDsl_Requirement  {

    private String text;





    private rqsDsl_Model rqsdsl_model;


    public rqsDsl_Requirement(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public rqsDsl_Model getRqsdsl_model() {
        return rqsdsl_model;
    }

    public void setRqsdsl_model(rqsDsl_Model rqsdsl_model) {
        this.rqsdsl_model = rqsdsl_model;
    }

}