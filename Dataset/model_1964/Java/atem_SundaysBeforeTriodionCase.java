





import java.util.List;
import java.util.ArrayList;

public class atem_SundaysBeforeTriodionCase  {

    private int dsl_SundaysBeforeTriodionCase_Days;





    private atem_WhenSundaysBeforeTriodion atem_whensundaysbeforetriodion;




    private List<atem_AbstractComponent> atem_abstractcomponents;


    public atem_SundaysBeforeTriodionCase(
        int dsl_SundaysBeforeTriodionCase_Days    ) {
        this.dsl_SundaysBeforeTriodionCase_Days = dsl_SundaysBeforeTriodionCase_Days;
        this.atem_abstractcomponents = new ArrayList<>();
    }

    public atem_SundaysBeforeTriodionCase(
        int dsl_SundaysBeforeTriodionCase_Days        ArrayList<atem_AbstractComponent> atem_abstractcomponents    ) {
        this.dsl_SundaysBeforeTriodionCase_Days = dsl_SundaysBeforeTriodionCase_Days;
        this.atem_abstractcomponents = atem_abstractcomponents;
    }

    public int getDsl_sundaysbeforetriodioncase_days() {
        return dsl_SundaysBeforeTriodionCase_Days;
    }

    public void setDsl_sundaysbeforetriodioncase_days(int dsl_SundaysBeforeTriodionCase_Days) {
        this.dsl_SundaysBeforeTriodionCase_Days = dsl_SundaysBeforeTriodionCase_Days;
    }

    public atem_WhenSundaysBeforeTriodion getAtem_whensundaysbeforetriodion() {
        return atem_whensundaysbeforetriodion;
    }

    public void setAtem_whensundaysbeforetriodion(atem_WhenSundaysBeforeTriodion atem_whensundaysbeforetriodion) {
        this.atem_whensundaysbeforetriodion = atem_whensundaysbeforetriodion;
    }
    public List<atem_AbstractComponent> getAtem_abstractcomponents() {
        return atem_abstractcomponents;
    }

    public void addAtem_abstractcomponent(Atem_abstractcomponent atem_abstractcomponent) {
        this.atem_abstractcomponents.add(atem_abstractcomponent);
    }

}