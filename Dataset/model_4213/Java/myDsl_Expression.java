





import java.util.List;
import java.util.ArrayList;

public class myDsl_Expression  {

    private int value;





    private myDsl_Model mydsl_model;


    public myDsl_Expression(
        int value    ) {
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public myDsl_Model getMydsl_model() {
        return mydsl_model;
    }

    public void setMydsl_model(myDsl_Model mydsl_model) {
        this.mydsl_model = mydsl_model;
    }

}