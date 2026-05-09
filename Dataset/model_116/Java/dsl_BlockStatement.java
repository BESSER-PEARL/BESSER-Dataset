





import java.util.List;
import java.util.ArrayList;

public class dsl_BlockStatement  {






    private dsl_ClassOrInterfaceDeclaration dsl_classorinterfacedeclaration;




    private dsl_MethodOrCtorDeclaration dsl_methodorctordeclaration;


    public dsl_BlockStatement(
    ) {
    }



    public dsl_ClassOrInterfaceDeclaration getDsl_classorinterfacedeclaration() {
        return dsl_classorinterfacedeclaration;
    }

    public void setDsl_classorinterfacedeclaration(dsl_ClassOrInterfaceDeclaration dsl_classorinterfacedeclaration) {
        this.dsl_classorinterfacedeclaration = dsl_classorinterfacedeclaration;
    }
    public dsl_MethodOrCtorDeclaration getDsl_methodorctordeclaration() {
        return dsl_methodorctordeclaration;
    }

    public void setDsl_methodorctordeclaration(dsl_MethodOrCtorDeclaration dsl_methodorctordeclaration) {
        this.dsl_methodorctordeclaration = dsl_methodorctordeclaration;
    }

}