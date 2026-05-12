





import java.util.List;
import java.util.ArrayList;

public class latex_Title  {

    private String authortext;
    private String titletext;
    private String titleprefix;





    private latex_Document latex_document;


    public latex_Title(
        String authortext,        String titletext,        String titleprefix    ) {
        this.authortext = authortext;
        this.titletext = titletext;
        this.titleprefix = titleprefix;
    }


    public String getAuthortext() {
        return authortext;
    }

    public void setAuthortext(String authortext) {
        this.authortext = authortext;
    }
    public String getTitletext() {
        return titletext;
    }

    public void setTitletext(String titletext) {
        this.titletext = titletext;
    }
    public String getTitleprefix() {
        return titleprefix;
    }

    public void setTitleprefix(String titleprefix) {
        this.titleprefix = titleprefix;
    }

    public latex_Document getLatex_document() {
        return latex_document;
    }

    public void setLatex_document(latex_Document latex_document) {
        this.latex_document = latex_document;
    }

}