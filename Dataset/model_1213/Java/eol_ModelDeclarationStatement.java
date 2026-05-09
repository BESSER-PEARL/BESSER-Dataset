





import java.util.List;
import java.util.ArrayList;

public class eol_ModelDeclarationStatement extends Statement {






    private eol_IModel eol_imodel;




    private eol_EOLLibraryModule eol_eollibrarymodule;




    private eol_NameExpression eol_nameexpression;


    public eol_ModelDeclarationStatement(
    ) {
        super(
        );
    }



    public eol_IModel getEol_imodel() {
        return eol_imodel;
    }

    public void setEol_imodel(eol_IModel eol_imodel) {
        this.eol_imodel = eol_imodel;
    }
    public eol_EOLLibraryModule getEol_eollibrarymodule() {
        return eol_eollibrarymodule;
    }

    public void setEol_eollibrarymodule(eol_EOLLibraryModule eol_eollibrarymodule) {
        this.eol_eollibrarymodule = eol_eollibrarymodule;
    }
    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }

}