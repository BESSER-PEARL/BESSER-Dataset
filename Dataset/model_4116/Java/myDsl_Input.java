





import java.util.List;
import java.util.ArrayList;

public class myDsl_Input  {

    private String var1;
    private String var2;





    private myDsl_Fonction mydsl_fonction;


    public myDsl_Input(
        String var1,        String var2    ) {
        this.var1 = var1;
        this.var2 = var2;
    }


    public String getVar1() {
        return var1;
    }

    public void setVar1(String var1) {
        this.var1 = var1;
    }
    public String getVar2() {
        return var2;
    }

    public void setVar2(String var2) {
        this.var2 = var2;
    }

    public myDsl_Fonction getMydsl_fonction() {
        return mydsl_fonction;
    }

    public void setMydsl_fonction(myDsl_Fonction mydsl_fonction) {
        this.mydsl_fonction = mydsl_fonction;
    }

}