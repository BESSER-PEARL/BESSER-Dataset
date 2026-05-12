





import java.util.List;
import java.util.ArrayList;

public class latex_Packages  {

    private String packageprefix;
    private String packagetype;





    private latex_Document latex_document;


    public latex_Packages(
        String packageprefix,        String packagetype    ) {
        this.packageprefix = packageprefix;
        this.packagetype = packagetype;
    }


    public String getPackageprefix() {
        return packageprefix;
    }

    public void setPackageprefix(String packageprefix) {
        this.packageprefix = packageprefix;
    }
    public String getPackagetype() {
        return packagetype;
    }

    public void setPackagetype(String packagetype) {
        this.packagetype = packagetype;
    }

    public latex_Document getLatex_document() {
        return latex_document;
    }

    public void setLatex_document(latex_Document latex_document) {
        this.latex_document = latex_document;
    }

}