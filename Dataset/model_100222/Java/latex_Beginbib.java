





import java.util.List;
import java.util.ArrayList;

public class latex_Beginbib  {

    private String Beginbibprefix;





    private latex_Bibliography latex_bibliography;


    public latex_Beginbib(
        String Beginbibprefix    ) {
        this.Beginbibprefix = Beginbibprefix;
    }


    public String getBeginbibprefix() {
        return Beginbibprefix;
    }

    public void setBeginbibprefix(String Beginbibprefix) {
        this.Beginbibprefix = Beginbibprefix;
    }

    public latex_Bibliography getLatex_bibliography() {
        return latex_bibliography;
    }

    public void setLatex_bibliography(latex_Bibliography latex_bibliography) {
        this.latex_bibliography = latex_bibliography;
    }

}