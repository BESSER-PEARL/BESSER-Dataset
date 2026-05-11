





import java.util.List;
import java.util.ArrayList;

public class siddhi_AS  {

    private String a;





    private siddhi_MainSource siddhi_mainsource;




    private siddhi_Keyword siddhi_keyword;




    private siddhi_OutAttr siddhi_outattr;


    public siddhi_AS(
        String a    ) {
        this.a = a;
    }


    public String getA() {
        return a;
    }

    public void setA(String a) {
        this.a = a;
    }

    public siddhi_MainSource getSiddhi_mainsource() {
        return siddhi_mainsource;
    }

    public void setSiddhi_mainsource(siddhi_MainSource siddhi_mainsource) {
        this.siddhi_mainsource = siddhi_mainsource;
    }
    public siddhi_Keyword getSiddhi_keyword() {
        return siddhi_keyword;
    }

    public void setSiddhi_keyword(siddhi_Keyword siddhi_keyword) {
        this.siddhi_keyword = siddhi_keyword;
    }
    public siddhi_OutAttr getSiddhi_outattr() {
        return siddhi_outattr;
    }

    public void setSiddhi_outattr(siddhi_OutAttr siddhi_outattr) {
        this.siddhi_outattr = siddhi_outattr;
    }

}