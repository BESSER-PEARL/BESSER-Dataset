





import java.util.List;
import java.util.ArrayList;

public class eol_Program extends EolElement {






    private List<eol_ModelDeclarationStatement> eol_modeldeclarationstatements;




    private List<eol_Program> eol_programs;




    private eol_NameExpression eol_nameexpression;


    public eol_Program(
    ) {
        super(
        );
        this.eol_modeldeclarationstatements = new ArrayList<>();
        this.eol_programs = new ArrayList<>();
    }

    public eol_Program(
        ArrayList<eol_ModelDeclarationStatement> eol_modeldeclarationstatements,        ArrayList<eol_Program> eol_programs    ) {
        this.eol_modeldeclarationstatements = eol_modeldeclarationstatements;
        this.eol_programs = eol_programs;
    }


    public List<eol_ModelDeclarationStatement> getEol_modeldeclarationstatements() {
        return eol_modeldeclarationstatements;
    }

    public void addEol_modeldeclarationstatement(Eol_modeldeclarationstatement eol_modeldeclarationstatement) {
        this.eol_modeldeclarationstatements.add(eol_modeldeclarationstatement);
    }
    public List<eol_Program> getEol_programs() {
        return eol_programs;
    }

    public void addEol_program(Eol_program eol_program) {
        this.eol_programs.add(eol_program);
    }
    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }

}