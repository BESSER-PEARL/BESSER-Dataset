





import java.util.List;
import java.util.ArrayList;

public class opf_Itemref  {

    private String linear;
    private String idref;



    public opf_Itemref(
        String linear,        String idref    ) {
        this.linear = linear;
        this.idref = idref;
    }


    public String getLinear() {
        return linear;
    }

    public void setLinear(String linear) {
        this.linear = linear;
    }
    public String getIdref() {
        return idref;
    }

    public void setIdref(String idref) {
        this.idref = idref;
    }


}