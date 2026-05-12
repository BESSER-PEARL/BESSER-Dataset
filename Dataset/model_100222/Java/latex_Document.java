





import java.util.List;
import java.util.ArrayList;

public class latex_Document  {

    private String documenttype;
    private String fontsize;
    private String papertype;
    private String prefix;





    private List<latex_Styles> latex_styless;




    private latex_Abstracte latex_abstracte;


    public latex_Document(
        String documenttype,        String fontsize,        String papertype,        String prefix    ) {
        this.documenttype = documenttype;
        this.fontsize = fontsize;
        this.papertype = papertype;
        this.prefix = prefix;
        this.latex_styless = new ArrayList<>();
    }

    public latex_Document(
        String documenttype,        String fontsize,        String papertype,        String prefix        ArrayList<latex_Styles> latex_styless    ) {
        this.documenttype = documenttype;
        this.fontsize = fontsize;
        this.papertype = papertype;
        this.prefix = prefix;
        this.latex_styless = latex_styless;
    }

    public String getDocumenttype() {
        return documenttype;
    }

    public void setDocumenttype(String documenttype) {
        this.documenttype = documenttype;
    }
    public String getFontsize() {
        return fontsize;
    }

    public void setFontsize(String fontsize) {
        this.fontsize = fontsize;
    }
    public String getPapertype() {
        return papertype;
    }

    public void setPapertype(String papertype) {
        this.papertype = papertype;
    }
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }

    public List<latex_Styles> getLatex_styless() {
        return latex_styless;
    }

    public void addLatex_styles(Latex_styles latex_styles) {
        this.latex_styless.add(latex_styles);
    }
    public latex_Abstracte getLatex_abstracte() {
        return latex_abstracte;
    }

    public void setLatex_abstracte(latex_Abstracte latex_abstracte) {
        this.latex_abstracte = latex_abstracte;
    }

}