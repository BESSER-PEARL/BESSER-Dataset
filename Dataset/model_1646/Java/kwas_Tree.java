





import java.util.List;
import java.util.ArrayList;

public class kwas_Tree  {

    private int valsS;
    private String labelI;
    private int valsI;
    private String labelS;





    private kwas_Top kwas_top;


    public kwas_Tree(
        int valsS,        String labelI,        int valsI,        String labelS    ) {
        this.valsS = valsS;
        this.labelI = labelI;
        this.valsI = valsI;
        this.labelS = labelS;
    }


    public int getValss() {
        return valsS;
    }

    public void setValss(int valsS) {
        this.valsS = valsS;
    }
    public String getLabeli() {
        return labelI;
    }

    public void setLabeli(String labelI) {
        this.labelI = labelI;
    }
    public int getValsi() {
        return valsI;
    }

    public void setValsi(int valsI) {
        this.valsI = valsI;
    }
    public String getLabels() {
        return labelS;
    }

    public void setLabels(String labelS) {
        this.labelS = labelS;
    }

    public kwas_Top getKwas_top() {
        return kwas_top;
    }

    public void setKwas_top(kwas_Top kwas_top) {
        this.kwas_top = kwas_top;
    }

}