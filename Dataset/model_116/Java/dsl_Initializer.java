





import java.util.List;
import java.util.ArrayList;

public class dsl_Initializer  {

    private boolean static;





    private dsl_ClassOrInterfaceBodyDeclaration dsl_classorinterfacebodydeclaration;


    public dsl_Initializer(
        boolean static    ) {
        this.static = static;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public dsl_ClassOrInterfaceBodyDeclaration getDsl_classorinterfacebodydeclaration() {
        return dsl_classorinterfacebodydeclaration;
    }

    public void setDsl_classorinterfacebodydeclaration(dsl_ClassOrInterfaceBodyDeclaration dsl_classorinterfacebodydeclaration) {
        this.dsl_classorinterfacebodydeclaration = dsl_classorinterfacebodydeclaration;
    }

}