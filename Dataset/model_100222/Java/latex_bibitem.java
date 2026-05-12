





import java.util.List;
import java.util.ArrayList;

public class latex_bibitem  {

    private String bibprefix;
    private String bibtext;





    private latex_Bibliography latex_bibliography;


    public latex_bibitem(
        String bibprefix,        String bibtext    ) {
        this.bibprefix = bibprefix;
        this.bibtext = bibtext;
    }


    public String getBibprefix() {
        return bibprefix;
    }

    public void setBibprefix(String bibprefix) {
        this.bibprefix = bibprefix;
    }
    public String getBibtext() {
        return bibtext;
    }

    public void setBibtext(String bibtext) {
        this.bibtext = bibtext;
    }

    public latex_Bibliography getLatex_bibliography() {
        return latex_bibliography;
    }

    public void setLatex_bibliography(latex_Bibliography latex_bibliography) {
        this.latex_bibliography = latex_bibliography;
    }

}