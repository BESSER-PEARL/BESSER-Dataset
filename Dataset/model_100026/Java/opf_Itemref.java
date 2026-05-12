





import java.util.List;
import java.util.ArrayList;

public class opf_Itemref  {

    private String idref;
    private String linear;





    private opf_Spine opf_spine;


    public opf_Itemref(
        String idref,        String linear    ) {
        this.idref = idref;
        this.linear = linear;
    }


    public String getIdref() {
        return idref;
    }

    public void setIdref(String idref) {
        this.idref = idref;
    }
    public String getLinear() {
        return linear;
    }

    public void setLinear(String linear) {
        this.linear = linear;
    }

    public opf_Spine getOpf_spine() {
        return opf_spine;
    }

    public void setOpf_spine(opf_Spine opf_spine) {
        this.opf_spine = opf_spine;
    }

}