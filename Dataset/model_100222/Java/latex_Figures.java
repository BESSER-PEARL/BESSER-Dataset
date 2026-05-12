





import java.util.List;
import java.util.ArrayList;

public class latex_Figures  {

    private String figname;
    private String figprefix;
    private String figcaption;





    private latex_Body latex_body;




    private List<latex_General> latex_generals;


    public latex_Figures(
        String figname,        String figprefix,        String figcaption    ) {
        this.figname = figname;
        this.figprefix = figprefix;
        this.figcaption = figcaption;
        this.latex_generals = new ArrayList<>();
    }

    public latex_Figures(
        String figname,        String figprefix,        String figcaption        ArrayList<latex_General> latex_generals    ) {
        this.figname = figname;
        this.figprefix = figprefix;
        this.figcaption = figcaption;
        this.latex_generals = latex_generals;
    }

    public String getFigname() {
        return figname;
    }

    public void setFigname(String figname) {
        this.figname = figname;
    }
    public String getFigprefix() {
        return figprefix;
    }

    public void setFigprefix(String figprefix) {
        this.figprefix = figprefix;
    }
    public String getFigcaption() {
        return figcaption;
    }

    public void setFigcaption(String figcaption) {
        this.figcaption = figcaption;
    }

    public latex_Body getLatex_body() {
        return latex_body;
    }

    public void setLatex_body(latex_Body latex_body) {
        this.latex_body = latex_body;
    }
    public List<latex_General> getLatex_generals() {
        return latex_generals;
    }

    public void addLatex_general(Latex_general latex_general) {
        this.latex_generals.add(latex_general);
    }

}