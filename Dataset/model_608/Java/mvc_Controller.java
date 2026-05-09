





import java.util.List;
import java.util.ArrayList;

public class mvc_Controller  {

    private String name;





    private mvc_Model mvc_model;




    private mvc_Model mvc_model;




    private mvc_View mvc_view;




    private mvc_MvcApplication mvc_mvcapplication;




    private mvc_View mvc_view;


    public mvc_Controller(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mvc_Model getMvc_model() {
        return mvc_model;
    }

    public void setMvc_model(mvc_Model mvc_model) {
        this.mvc_model = mvc_model;
    }
    public mvc_Model getMvc_model() {
        return mvc_model;
    }

    public void setMvc_model(mvc_Model mvc_model) {
        this.mvc_model = mvc_model;
    }
    public mvc_View getMvc_view() {
        return mvc_view;
    }

    public void setMvc_view(mvc_View mvc_view) {
        this.mvc_view = mvc_view;
    }
    public mvc_MvcApplication getMvc_mvcapplication() {
        return mvc_mvcapplication;
    }

    public void setMvc_mvcapplication(mvc_MvcApplication mvc_mvcapplication) {
        this.mvc_mvcapplication = mvc_mvcapplication;
    }
    public mvc_View getMvc_view() {
        return mvc_view;
    }

    public void setMvc_view(mvc_View mvc_view) {
        this.mvc_view = mvc_view;
    }

}