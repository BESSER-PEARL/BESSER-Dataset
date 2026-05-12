





import java.util.List;
import java.util.ArrayList;

public class latex_Begin  {

    private String beginprefix;





    private latex_Document latex_document;


    public latex_Begin(
        String beginprefix    ) {
        this.beginprefix = beginprefix;
    }


    public String getBeginprefix() {
        return beginprefix;
    }

    public void setBeginprefix(String beginprefix) {
        this.beginprefix = beginprefix;
    }

    public latex_Document getLatex_document() {
        return latex_document;
    }

    public void setLatex_document(latex_Document latex_document) {
        this.latex_document = latex_document;
    }

}