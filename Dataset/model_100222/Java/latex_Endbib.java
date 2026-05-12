





import java.util.List;
import java.util.ArrayList;

public class latex_Endbib  {

    private String Endbibprefix;





    private latex_Bibliography latex_bibliography;


    public latex_Endbib(
        String Endbibprefix    ) {
        this.Endbibprefix = Endbibprefix;
    }


    public String getEndbibprefix() {
        return Endbibprefix;
    }

    public void setEndbibprefix(String Endbibprefix) {
        this.Endbibprefix = Endbibprefix;
    }

    public latex_Bibliography getLatex_bibliography() {
        return latex_bibliography;
    }

    public void setLatex_bibliography(latex_Bibliography latex_bibliography) {
        this.latex_bibliography = latex_bibliography;
    }

}