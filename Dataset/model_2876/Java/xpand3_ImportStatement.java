





import java.util.List;
import java.util.ArrayList;

public class xpand3_ImportStatement extends SyntaxElement {

    private boolean exported;





    private xpand3_Identifier xpand3_identifier;




    private xpand3_File xpand3_file;


    public xpand3_ImportStatement(
        boolean exported    ) {
        super(
        );
        this.exported = exported;
    }


    public boolean getExported() {
        return exported;
    }

    public void setExported(boolean exported) {
        this.exported = exported;
    }

    public xpand3_Identifier getXpand3_identifier() {
        return xpand3_identifier;
    }

    public void setXpand3_identifier(xpand3_Identifier xpand3_identifier) {
        this.xpand3_identifier = xpand3_identifier;
    }
    public xpand3_File getXpand3_file() {
        return xpand3_file;
    }

    public void setXpand3_file(xpand3_File xpand3_file) {
        this.xpand3_file = xpand3_file;
    }

}