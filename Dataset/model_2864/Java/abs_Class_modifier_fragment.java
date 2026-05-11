





import java.util.List;
import java.util.ArrayList;

public class abs_Class_modifier_fragment  {






    private abs_OO_modifier abs_oo_modifier;




    private List<abs_Methodsig> abs_methodsigs;


    public abs_Class_modifier_fragment(
    ) {
        this.abs_methodsigs = new ArrayList<>();
    }

    public abs_Class_modifier_fragment(
        ArrayList<abs_Methodsig> abs_methodsigs    ) {
        this.abs_methodsigs = abs_methodsigs;
    }


    public abs_OO_modifier getAbs_oo_modifier() {
        return abs_oo_modifier;
    }

    public void setAbs_oo_modifier(abs_OO_modifier abs_oo_modifier) {
        this.abs_oo_modifier = abs_oo_modifier;
    }
    public List<abs_Methodsig> getAbs_methodsigs() {
        return abs_methodsigs;
    }

    public void addAbs_methodsig(Abs_methodsig abs_methodsig) {
        this.abs_methodsigs.add(abs_methodsig);
    }

}