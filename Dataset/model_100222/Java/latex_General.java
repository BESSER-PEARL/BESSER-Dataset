





import java.util.List;
import java.util.ArrayList;

public class latex_General  {

    private String genprefix;
    private String gentext;
    private String genname;





    private latex_Abstracte latex_abstracte;




    private latex_Title latex_title;




    private latex_Bibliography latex_bibliography;


    public latex_General(
        String genprefix,        String gentext,        String genname    ) {
        this.genprefix = genprefix;
        this.gentext = gentext;
        this.genname = genname;
    }


    public String getGenprefix() {
        return genprefix;
    }

    public void setGenprefix(String genprefix) {
        this.genprefix = genprefix;
    }
    public String getGentext() {
        return gentext;
    }

    public void setGentext(String gentext) {
        this.gentext = gentext;
    }
    public String getGenname() {
        return genname;
    }

    public void setGenname(String genname) {
        this.genname = genname;
    }

    public latex_Abstracte getLatex_abstracte() {
        return latex_abstracte;
    }

    public void setLatex_abstracte(latex_Abstracte latex_abstracte) {
        this.latex_abstracte = latex_abstracte;
    }
    public latex_Title getLatex_title() {
        return latex_title;
    }

    public void setLatex_title(latex_Title latex_title) {
        this.latex_title = latex_title;
    }
    public latex_Bibliography getLatex_bibliography() {
        return latex_bibliography;
    }

    public void setLatex_bibliography(latex_Bibliography latex_bibliography) {
        this.latex_bibliography = latex_bibliography;
    }

}