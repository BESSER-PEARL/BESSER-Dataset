





import java.util.List;
import java.util.ArrayList;

public class sADL_ValueRow  {






    private List<sADL_Expression> sadl_expressions;




    private sADL_ValueTable sadl_valuetable;




    private sADL_ValueTable sadl_valuetable;


    public sADL_ValueRow(
    ) {
        this.sadl_expressions = new ArrayList<>();
    }

    public sADL_ValueRow(
        ArrayList<sADL_Expression> sadl_expressions    ) {
        this.sadl_expressions = sadl_expressions;
    }


    public List<sADL_Expression> getSadl_expressions() {
        return sadl_expressions;
    }

    public void addSadl_expression(Sadl_expression sadl_expression) {
        this.sadl_expressions.add(sadl_expression);
    }
    public sADL_ValueTable getSadl_valuetable() {
        return sadl_valuetable;
    }

    public void setSadl_valuetable(sADL_ValueTable sadl_valuetable) {
        this.sadl_valuetable = sadl_valuetable;
    }
    public sADL_ValueTable getSadl_valuetable() {
        return sadl_valuetable;
    }

    public void setSadl_valuetable(sADL_ValueTable sadl_valuetable) {
        this.sadl_valuetable = sadl_valuetable;
    }

}