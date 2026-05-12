





import java.util.List;
import java.util.ArrayList;

public class latex_Bibliography  {

    private String bibstyle;





    private latex_Document latex_document;


    public latex_Bibliography(
        String bibstyle    ) {
        this.bibstyle = bibstyle;
    }


    public String getBibstyle() {
        return bibstyle;
    }

    public void setBibstyle(String bibstyle) {
        this.bibstyle = bibstyle;
    }

    public latex_Document getLatex_document() {
        return latex_document;
    }

    public void setLatex_document(latex_Document latex_document) {
        this.latex_document = latex_document;
    }

}