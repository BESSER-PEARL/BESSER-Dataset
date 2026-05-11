





import java.util.List;
import java.util.ArrayList;

public class myDsl_Output  {

    private String out;





    private myDsl_Fonction mydsl_fonction;


    public myDsl_Output(
        String out    ) {
        this.out = out;
    }


    public String getOut() {
        return out;
    }

    public void setOut(String out) {
        this.out = out;
    }

    public myDsl_Fonction getMydsl_fonction() {
        return mydsl_fonction;
    }

    public void setMydsl_fonction(myDsl_Fonction mydsl_fonction) {
        this.mydsl_fonction = mydsl_fonction;
    }

}