





import java.util.List;
import java.util.ArrayList;

public class JAVA_FieldDeclaration extends BodyDeclaration {






    private JAVA_TypeAccess java_typeaccess;




    private JAVA_ClassDeclaration java_classdeclaration;


    public JAVA_FieldDeclaration(
    ) {
        super(
        );
    }



    public JAVA_TypeAccess getJava_typeaccess() {
        return java_typeaccess;
    }

    public void setJava_typeaccess(JAVA_TypeAccess java_typeaccess) {
        this.java_typeaccess = java_typeaccess;
    }
    public JAVA_ClassDeclaration getJava_classdeclaration() {
        return java_classdeclaration;
    }

    public void setJava_classdeclaration(JAVA_ClassDeclaration java_classdeclaration) {
        this.java_classdeclaration = java_classdeclaration;
    }

}