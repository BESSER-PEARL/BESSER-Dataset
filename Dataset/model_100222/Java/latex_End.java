





import java.util.List;
import java.util.ArrayList;

public class latex_End  {

    private String endprefix;





    private latex_Document latex_document;


    public latex_End(
        String endprefix    ) {
        this.endprefix = endprefix;
    }


    public String getEndprefix() {
        return endprefix;
    }

    public void setEndprefix(String endprefix) {
        this.endprefix = endprefix;
    }

    public latex_Document getLatex_document() {
        return latex_document;
    }

    public void setLatex_document(latex_Document latex_document) {
        this.latex_document = latex_document;
    }

}