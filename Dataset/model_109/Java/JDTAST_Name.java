





import java.util.List;
import java.util.ArrayList;

public class JDTAST_Name extends Expression {

    private String fullyQualifiedName;





    private JDTAST_MethodRef jdtast_methodref;




    private JDTAST_ImportDeclaration jdtast_importdeclaration;




    private JDTAST_PackageDeclaration jdtast_packagedeclaration;




    private JDTAST_MemberRef jdtast_memberref;


    public JDTAST_Name(
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

    public JDTAST_MethodRef getJdtast_methodref() {
        return jdtast_methodref;
    }

    public void setJdtast_methodref(JDTAST_MethodRef jdtast_methodref) {
        this.jdtast_methodref = jdtast_methodref;
    }
    public JDTAST_ImportDeclaration getJdtast_importdeclaration() {
        return jdtast_importdeclaration;
    }

    public void setJdtast_importdeclaration(JDTAST_ImportDeclaration jdtast_importdeclaration) {
        this.jdtast_importdeclaration = jdtast_importdeclaration;
    }
    public JDTAST_PackageDeclaration getJdtast_packagedeclaration() {
        return jdtast_packagedeclaration;
    }

    public void setJdtast_packagedeclaration(JDTAST_PackageDeclaration jdtast_packagedeclaration) {
        this.jdtast_packagedeclaration = jdtast_packagedeclaration;
    }
    public JDTAST_MemberRef getJdtast_memberref() {
        return jdtast_memberref;
    }

    public void setJdtast_memberref(JDTAST_MemberRef jdtast_memberref) {
        this.jdtast_memberref = jdtast_memberref;
    }

}