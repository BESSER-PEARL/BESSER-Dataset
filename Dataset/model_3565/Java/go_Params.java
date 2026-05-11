





import java.util.List;
import java.util.ArrayList;

public class go_Params  {

    private String type;
    private String params;





    private go_CallFunc go_callfunc;




    private go_DecFunc go_decfunc;


    public go_Params(
        String type,        String params    ) {
        this.type = type;
        this.params = params;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getParams() {
        return params;
    }

    public void setParams(String params) {
        this.params = params;
    }

    public go_CallFunc getGo_callfunc() {
        return go_callfunc;
    }

    public void setGo_callfunc(go_CallFunc go_callfunc) {
        this.go_callfunc = go_callfunc;
    }
    public go_DecFunc getGo_decfunc() {
        return go_decfunc;
    }

    public void setGo_decfunc(go_DecFunc go_decfunc) {
        this.go_decfunc = go_decfunc;
    }

}