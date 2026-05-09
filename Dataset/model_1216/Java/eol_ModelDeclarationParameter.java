





import java.util.List;
import java.util.ArrayList;

public class eol_ModelDeclarationParameter extends EolElement {






    private eol_StringExpression eol_stringexpression;




    private eol_ModelDeclarationStatement eol_modeldeclarationstatement;




    private eol_NameExpression eol_nameexpression;


    public eol_ModelDeclarationParameter(
    ) {
        super(
        );
    }



    public eol_StringExpression getEol_stringexpression() {
        return eol_stringexpression;
    }

    public void setEol_stringexpression(eol_StringExpression eol_stringexpression) {
        this.eol_stringexpression = eol_stringexpression;
    }
    public eol_ModelDeclarationStatement getEol_modeldeclarationstatement() {
        return eol_modeldeclarationstatement;
    }

    public void setEol_modeldeclarationstatement(eol_ModelDeclarationStatement eol_modeldeclarationstatement) {
        this.eol_modeldeclarationstatement = eol_modeldeclarationstatement;
    }
    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }

}