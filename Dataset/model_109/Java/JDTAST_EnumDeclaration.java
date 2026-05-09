





import java.util.List;
import java.util.ArrayList;

public class JDTAST_EnumDeclaration extends AbstractTypeDeclaration {






    private List<JDTAST_Type> jdtast_types;




    private List<JDTAST_EnumConstantDeclaration> jdtast_enumconstantdeclarations;


    public JDTAST_EnumDeclaration(
    ) {
        super(
        );
        this.jdtast_types = new ArrayList<>();
        this.jdtast_enumconstantdeclarations = new ArrayList<>();
    }

    public JDTAST_EnumDeclaration(
        ArrayList<JDTAST_Type> jdtast_types,        ArrayList<JDTAST_EnumConstantDeclaration> jdtast_enumconstantdeclarations    ) {
        this.jdtast_types = jdtast_types;
        this.jdtast_enumconstantdeclarations = jdtast_enumconstantdeclarations;
    }


    public List<JDTAST_Type> getJdtast_types() {
        return jdtast_types;
    }

    public void addJdtast_type(Jdtast_type jdtast_type) {
        this.jdtast_types.add(jdtast_type);
    }
    public List<JDTAST_EnumConstantDeclaration> getJdtast_enumconstantdeclarations() {
        return jdtast_enumconstantdeclarations;
    }

    public void addJdtast_enumconstantdeclaration(Jdtast_enumconstantdeclaration jdtast_enumconstantdeclaration) {
        this.jdtast_enumconstantdeclarations.add(jdtast_enumconstantdeclaration);
    }

}