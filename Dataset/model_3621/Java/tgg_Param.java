





import java.util.List;
import java.util.ArrayList;

public class tgg_Param  {

    private String paramName;





    private tgg_AttrCondDef tgg_attrconddef;


    public tgg_Param(
        String paramName    ) {
        this.paramName = paramName;
    }


    public String getParamname() {
        return paramName;
    }

    public void setParamname(String paramName) {
        this.paramName = paramName;
    }

    public tgg_AttrCondDef getTgg_attrconddef() {
        return tgg_attrconddef;
    }

    public void setTgg_attrconddef(tgg_AttrCondDef tgg_attrconddef) {
        this.tgg_attrconddef = tgg_attrconddef;
    }

}