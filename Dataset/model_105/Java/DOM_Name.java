





import java.util.List;
import java.util.ArrayList;

public class DOM_Name extends Expression {

    private String fullyQualifiedName;





    private DOM_PackageDeclaration dom_packagedeclaration;




    private DOM_MethodRef dom_methodref;




    private DOM_ImportDeclaration dom_importdeclaration;




    private DOM_MemberRef dom_memberref;


    public DOM_Name(
        String fullyQualifiedName    ) {
        super(
        );
        this.fullyQualifiedName = fullyQualifiedName;
    }


    public String getFullyqualifiedname() {
        return fullyQualifiedName;
    }

    public void setFullyqualifiedname(String fullyQualifiedName) {
        this.fullyQualifiedName = fullyQualifiedName;
    }

    public DOM_PackageDeclaration getDom_packagedeclaration() {
        return dom_packagedeclaration;
    }

    public void setDom_packagedeclaration(DOM_PackageDeclaration dom_packagedeclaration) {
        this.dom_packagedeclaration = dom_packagedeclaration;
    }
    public DOM_MethodRef getDom_methodref() {
        return dom_methodref;
    }

    public void setDom_methodref(DOM_MethodRef dom_methodref) {
        this.dom_methodref = dom_methodref;
    }
    public DOM_ImportDeclaration getDom_importdeclaration() {
        return dom_importdeclaration;
    }

    public void setDom_importdeclaration(DOM_ImportDeclaration dom_importdeclaration) {
        this.dom_importdeclaration = dom_importdeclaration;
    }
    public DOM_MemberRef getDom_memberref() {
        return dom_memberref;
    }

    public void setDom_memberref(DOM_MemberRef dom_memberref) {
        this.dom_memberref = dom_memberref;
    }

}