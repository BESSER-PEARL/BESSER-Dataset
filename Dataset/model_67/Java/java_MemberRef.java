





import java.util.List;
import java.util.ArrayList;

public class java_MemberRef extends ASTNode {






    private java_TypeAccess java_typeaccess;




    private java_NamedElement java_namedelement;


    public java_MemberRef(
    ) {
        super(
        );
    }



    public java_TypeAccess getJava_typeaccess() {
        return java_typeaccess;
    }

    public void setJava_typeaccess(java_TypeAccess java_typeaccess) {
        this.java_typeaccess = java_typeaccess;
    }
    public java_NamedElement getJava_namedelement() {
        return java_namedelement;
    }

    public void setJava_namedelement(java_NamedElement java_namedelement) {
        this.java_namedelement = java_namedelement;
    }

}