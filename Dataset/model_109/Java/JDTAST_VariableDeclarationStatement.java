





import java.util.List;
import java.util.ArrayList;

public class JDTAST_VariableDeclarationStatement extends Statement {






    private JDTAST_Type jdtast_type;




    private List<JDTAST_VariableDeclarationFragment> jdtast_variabledeclarationfragments;




    private List<JDTAST_ExtendedModifier> jdtast_extendedmodifiers;


    public JDTAST_VariableDeclarationStatement(
    ) {
        super(
        );
        this.jdtast_variabledeclarationfragments = new ArrayList<>();
        this.jdtast_extendedmodifiers = new ArrayList<>();
    }

    public JDTAST_VariableDeclarationStatement(
        ArrayList<JDTAST_VariableDeclarationFragment> jdtast_variabledeclarationfragments,        ArrayList<JDTAST_ExtendedModifier> jdtast_extendedmodifiers    ) {
        this.jdtast_variabledeclarationfragments = jdtast_variabledeclarationfragments;
        this.jdtast_extendedmodifiers = jdtast_extendedmodifiers;
    }


    public JDTAST_Type getJdtast_type() {
        return jdtast_type;
    }

    public void setJdtast_type(JDTAST_Type jdtast_type) {
        this.jdtast_type = jdtast_type;
    }
    public List<JDTAST_VariableDeclarationFragment> getJdtast_variabledeclarationfragments() {
        return jdtast_variabledeclarationfragments;
    }

    public void addJdtast_variabledeclarationfragment(Jdtast_variabledeclarationfragment jdtast_variabledeclarationfragment) {
        this.jdtast_variabledeclarationfragments.add(jdtast_variabledeclarationfragment);
    }
    public List<JDTAST_ExtendedModifier> getJdtast_extendedmodifiers() {
        return jdtast_extendedmodifiers;
    }

    public void addJdtast_extendedmodifier(Jdtast_extendedmodifier jdtast_extendedmodifier) {
        this.jdtast_extendedmodifiers.add(jdtast_extendedmodifier);
    }

}