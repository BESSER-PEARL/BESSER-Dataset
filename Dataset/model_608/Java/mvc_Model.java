





import java.util.List;
import java.util.ArrayList;

public class mvc_Model  {

    private String nameclass;
    private String type;





    private mvc_MvcApplication mvc_mvcapplication;


    public mvc_Model(
        String nameclass,        String type    ) {
        this.nameclass = nameclass;
        this.type = type;
    }


    public String getNameclass() {
        return nameclass;
    }

    public void setNameclass(String nameclass) {
        this.nameclass = nameclass;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public mvc_MvcApplication getMvc_mvcapplication() {
        return mvc_mvcapplication;
    }

    public void setMvc_mvcapplication(mvc_MvcApplication mvc_mvcapplication) {
        this.mvc_mvcapplication = mvc_mvcapplication;
    }

}