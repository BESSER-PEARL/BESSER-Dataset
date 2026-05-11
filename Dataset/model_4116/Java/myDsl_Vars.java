





import java.util.List;
import java.util.ArrayList;

public class myDsl_Vars  {

    private String var3;
    private String var2;





    private myDsl_AffectVar mydsl_affectvar;


    public myDsl_Vars(
        String var3,        String var2    ) {
        this.var3 = var3;
        this.var2 = var2;
    }


    public String getVar3() {
        return var3;
    }

    public void setVar3(String var3) {
        this.var3 = var3;
    }
    public String getVar2() {
        return var2;
    }

    public void setVar2(String var2) {
        this.var2 = var2;
    }

    public myDsl_AffectVar getMydsl_affectvar() {
        return mydsl_affectvar;
    }

    public void setMydsl_affectvar(myDsl_AffectVar mydsl_affectvar) {
        this.mydsl_affectvar = mydsl_affectvar;
    }

}