





import java.util.List;
import java.util.ArrayList;

public class latex_Commands  {

    private String comtext;
    private float number;
    private String comname;
    private String comprefix;





    private latex_Document latex_document;


    public latex_Commands(
        String comtext,        float number,        String comname,        String comprefix    ) {
        this.comtext = comtext;
        this.number = number;
        this.comname = comname;
        this.comprefix = comprefix;
    }


    public String getComtext() {
        return comtext;
    }

    public void setComtext(String comtext) {
        this.comtext = comtext;
    }
    public float getNumber() {
        return number;
    }

    public void setNumber(float number) {
        this.number = number;
    }
    public String getComname() {
        return comname;
    }

    public void setComname(String comname) {
        this.comname = comname;
    }
    public String getComprefix() {
        return comprefix;
    }

    public void setComprefix(String comprefix) {
        this.comprefix = comprefix;
    }

    public latex_Document getLatex_document() {
        return latex_document;
    }

    public void setLatex_document(latex_Document latex_document) {
        this.latex_document = latex_document;
    }

}