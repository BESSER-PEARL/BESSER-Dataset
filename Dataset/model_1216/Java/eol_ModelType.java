





import java.util.List;
import java.util.ArrayList;

public class eol_ModelType extends Type {






    private List<eol_ModelDeclarationStatement> eol_modeldeclarationstatements;




    private eol_NameExpression eol_nameexpression;


    public eol_ModelType(
    ) {
        super(
        );
        this.eol_modeldeclarationstatements = new ArrayList<>();
    }

    public eol_ModelType(
        ArrayList<eol_ModelDeclarationStatement> eol_modeldeclarationstatements    ) {
        this.eol_modeldeclarationstatements = eol_modeldeclarationstatements;
    }


    public List<eol_ModelDeclarationStatement> getEol_modeldeclarationstatements() {
        return eol_modeldeclarationstatements;
    }

    public void addEol_modeldeclarationstatement(Eol_modeldeclarationstatement eol_modeldeclarationstatement) {
        this.eol_modeldeclarationstatements.add(eol_modeldeclarationstatement);
    }
    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }

}