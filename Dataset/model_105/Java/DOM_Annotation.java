





import java.util.List;
import java.util.ArrayList;

public class DOM_Annotation extends Expression, ExtendedModifier {






    private DOM_PackageDeclaration dom_packagedeclaration;




    private DOM_Name dom_name;


    public DOM_Annotation(
    ) {
        super(
        );
    }



    public DOM_PackageDeclaration getDom_packagedeclaration() {
        return dom_packagedeclaration;
    }

    public void setDom_packagedeclaration(DOM_PackageDeclaration dom_packagedeclaration) {
        this.dom_packagedeclaration = dom_packagedeclaration;
    }
    public DOM_Name getDom_name() {
        return dom_name;
    }

    public void setDom_name(DOM_Name dom_name) {
        this.dom_name = dom_name;
    }

}