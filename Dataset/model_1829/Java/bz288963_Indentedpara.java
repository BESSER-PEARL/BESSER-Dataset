





import java.util.List;
import java.util.ArrayList;

public class bz288963_Indentedpara extends Paragraph {

    private String indentSpace;





    private bz288963_DocumentRoot bz288963_documentroot;


    public bz288963_Indentedpara(
        String indentSpace    ) {
        super(
        );
        this.indentSpace = indentSpace;
    }


    public String getIndentspace() {
        return indentSpace;
    }

    public void setIndentspace(String indentSpace) {
        this.indentSpace = indentSpace;
    }

    public bz288963_DocumentRoot getBz288963_documentroot() {
        return bz288963_documentroot;
    }

    public void setBz288963_documentroot(bz288963_DocumentRoot bz288963_documentroot) {
        this.bz288963_documentroot = bz288963_documentroot;
    }

}