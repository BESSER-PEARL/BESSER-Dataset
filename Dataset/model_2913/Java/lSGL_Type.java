





import java.util.List;
import java.util.ArrayList;

public class lSGL_Type  {

    private String name;





    private lSGL_AttributeType lsgl_attributetype;




    private lSGL_Model lsgl_model;


    public lSGL_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public lSGL_AttributeType getLsgl_attributetype() {
        return lsgl_attributetype;
    }

    public void setLsgl_attributetype(lSGL_AttributeType lsgl_attributetype) {
        this.lsgl_attributetype = lsgl_attributetype;
    }
    public lSGL_Model getLsgl_model() {
        return lsgl_model;
    }

    public void setLsgl_model(lSGL_Model lsgl_model) {
        this.lsgl_model = lsgl_model;
    }

}