





import java.util.List;
import java.util.ArrayList;

public class mvc_View extends Annotable {

    private String name;





    private mvc_UIComponent mvc_uicomponent;




    private mvc_ControllerView mvc_controllerview;




    private mvc_MVCModel mvc_mvcmodel;


    public mvc_View(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mvc_UIComponent getMvc_uicomponent() {
        return mvc_uicomponent;
    }

    public void setMvc_uicomponent(mvc_UIComponent mvc_uicomponent) {
        this.mvc_uicomponent = mvc_uicomponent;
    }
    public mvc_ControllerView getMvc_controllerview() {
        return mvc_controllerview;
    }

    public void setMvc_controllerview(mvc_ControllerView mvc_controllerview) {
        this.mvc_controllerview = mvc_controllerview;
    }
    public mvc_MVCModel getMvc_mvcmodel() {
        return mvc_mvcmodel;
    }

    public void setMvc_mvcmodel(mvc_MVCModel mvc_mvcmodel) {
        this.mvc_mvcmodel = mvc_mvcmodel;
    }

}