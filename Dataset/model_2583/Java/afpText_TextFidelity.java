





import java.util.List;
import java.util.ArrayList;

public class afpText_TextFidelity extends triplet {

    private String RepTxtEx;
    private String StpTxtEx;



    public afpText_TextFidelity(
        String RepTxtEx,        String StpTxtEx    ) {
        super(
        );
        this.RepTxtEx = RepTxtEx;
        this.StpTxtEx = StpTxtEx;
    }


    public String getReptxtex() {
        return RepTxtEx;
    }

    public void setReptxtex(String RepTxtEx) {
        this.RepTxtEx = RepTxtEx;
    }
    public String getStptxtex() {
        return StpTxtEx;
    }

    public void setStptxtex(String StpTxtEx) {
        this.StpTxtEx = StpTxtEx;
    }


}