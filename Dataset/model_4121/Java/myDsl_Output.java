





import java.util.List;
import java.util.ArrayList;

public class myDsl_Output  {

    private String v2;
    private String v;





    private myDsl_Definiton mydsl_definiton;


    public myDsl_Output(
        String v2,        String v    ) {
        this.v2 = v2;
        this.v = v;
    }


    public String getV2() {
        return v2;
    }

    public void setV2(String v2) {
        this.v2 = v2;
    }
    public String getV() {
        return v;
    }

    public void setV(String v) {
        this.v = v;
    }

    public myDsl_Definiton getMydsl_definiton() {
        return mydsl_definiton;
    }

    public void setMydsl_definiton(myDsl_Definiton mydsl_definiton) {
        this.mydsl_definiton = mydsl_definiton;
    }

}