





import java.util.List;
import java.util.ArrayList;

public class dsl_MethodOrCtorDeclaration  {

    private String id;





    private dsl_ClassOrInterfaceBodyDeclaration dsl_classorinterfacebodydeclaration;




    private dsl_TypeParameters dsl_typeparameters;


    public dsl_MethodOrCtorDeclaration(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dsl_ClassOrInterfaceBodyDeclaration getDsl_classorinterfacebodydeclaration() {
        return dsl_classorinterfacebodydeclaration;
    }

    public void setDsl_classorinterfacebodydeclaration(dsl_ClassOrInterfaceBodyDeclaration dsl_classorinterfacebodydeclaration) {
        this.dsl_classorinterfacebodydeclaration = dsl_classorinterfacebodydeclaration;
    }
    public dsl_TypeParameters getDsl_typeparameters() {
        return dsl_typeparameters;
    }

    public void setDsl_typeparameters(dsl_TypeParameters dsl_typeparameters) {
        this.dsl_typeparameters = dsl_typeparameters;
    }

}