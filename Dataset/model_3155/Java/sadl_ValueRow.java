





import java.util.List;
import java.util.ArrayList;

public class sadl_ValueRow  {






    private sadl_ExplicitValue sadl_explicitvalue;




    private List<sadl_ExplicitValue> sadl_explicitvalues;




    private sadl_ValueTable sadl_valuetable;


    public sadl_ValueRow(
    ) {
        this.sadl_explicitvalues = new ArrayList<>();
    }

    public sadl_ValueRow(
        ArrayList<sadl_ExplicitValue> sadl_explicitvalues    ) {
        this.sadl_explicitvalues = sadl_explicitvalues;
    }


    public sadl_ExplicitValue getSadl_explicitvalue() {
        return sadl_explicitvalue;
    }

    public void setSadl_explicitvalue(sadl_ExplicitValue sadl_explicitvalue) {
        this.sadl_explicitvalue = sadl_explicitvalue;
    }
    public List<sadl_ExplicitValue> getSadl_explicitvalues() {
        return sadl_explicitvalues;
    }

    public void addSadl_explicitvalue(Sadl_explicitvalue sadl_explicitvalue) {
        this.sadl_explicitvalues.add(sadl_explicitvalue);
    }
    public sadl_ValueTable getSadl_valuetable() {
        return sadl_valuetable;
    }

    public void setSadl_valuetable(sadl_ValueTable sadl_valuetable) {
        this.sadl_valuetable = sadl_valuetable;
    }

}