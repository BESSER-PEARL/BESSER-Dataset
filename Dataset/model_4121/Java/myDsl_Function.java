





import java.util.List;
import java.util.ArrayList;

public class myDsl_Function  {

    private String funName;





    private myDsl_Model mydsl_model;


    public myDsl_Function(
        String funName    ) {
        this.funName = funName;
    }


    public String getFunname() {
        return funName;
    }

    public void setFunname(String funName) {
        this.funName = funName;
    }

    public myDsl_Model getMydsl_model() {
        return mydsl_model;
    }

    public void setMydsl_model(myDsl_Model mydsl_model) {
        this.mydsl_model = mydsl_model;
    }

}