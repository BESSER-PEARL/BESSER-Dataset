





import java.util.List;
import java.util.ArrayList;

public class DOM_EnumDeclaration extends AbstractTypeDeclaration {






    private List<DOM_EnumConstantDeclaration> dom_enumconstantdeclarations;




    private List<DOM_Type> dom_types;


    public DOM_EnumDeclaration(
    ) {
        super(
        );
        this.dom_enumconstantdeclarations = new ArrayList<>();
        this.dom_types = new ArrayList<>();
    }

    public DOM_EnumDeclaration(
        ArrayList<DOM_EnumConstantDeclaration> dom_enumconstantdeclarations,        ArrayList<DOM_Type> dom_types    ) {
        this.dom_enumconstantdeclarations = dom_enumconstantdeclarations;
        this.dom_types = dom_types;
    }


    public List<DOM_EnumConstantDeclaration> getDom_enumconstantdeclarations() {
        return dom_enumconstantdeclarations;
    }

    public void addDom_enumconstantdeclaration(Dom_enumconstantdeclaration dom_enumconstantdeclaration) {
        this.dom_enumconstantdeclarations.add(dom_enumconstantdeclaration);
    }
    public List<DOM_Type> getDom_types() {
        return dom_types;
    }

    public void addDom_type(Dom_type dom_type) {
        this.dom_types.add(dom_type);
    }

}