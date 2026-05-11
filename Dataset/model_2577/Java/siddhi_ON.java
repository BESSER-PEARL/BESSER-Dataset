





import java.util.List;
import java.util.ArrayList;

public class siddhi_ON  {

    private String on;





    private siddhi_Keyword siddhi_keyword;




    private siddhi_QueryOutput siddhi_queryoutput;


    public siddhi_ON(
        String on    ) {
        this.on = on;
    }


    public String getOn() {
        return on;
    }

    public void setOn(String on) {
        this.on = on;
    }

    public siddhi_Keyword getSiddhi_keyword() {
        return siddhi_keyword;
    }

    public void setSiddhi_keyword(siddhi_Keyword siddhi_keyword) {
        this.siddhi_keyword = siddhi_keyword;
    }
    public siddhi_QueryOutput getSiddhi_queryoutput() {
        return siddhi_queryoutput;
    }

    public void setSiddhi_queryoutput(siddhi_QueryOutput siddhi_queryoutput) {
        this.siddhi_queryoutput = siddhi_queryoutput;
    }

}