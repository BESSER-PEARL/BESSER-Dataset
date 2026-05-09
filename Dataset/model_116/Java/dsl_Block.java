





import java.util.List;
import java.util.ArrayList;

public class dsl_Block  {






    private List<dsl_BlockStatement> dsl_blockstatements;




    private dsl_MethodOrCtorDeclaration dsl_methodorctordeclaration;




    private dsl_Initializer dsl_initializer;


    public dsl_Block(
    ) {
        this.dsl_blockstatements = new ArrayList<>();
    }

    public dsl_Block(
        ArrayList<dsl_BlockStatement> dsl_blockstatements    ) {
        this.dsl_blockstatements = dsl_blockstatements;
    }


    public List<dsl_BlockStatement> getDsl_blockstatements() {
        return dsl_blockstatements;
    }

    public void addDsl_blockstatement(Dsl_blockstatement dsl_blockstatement) {
        this.dsl_blockstatements.add(dsl_blockstatement);
    }
    public dsl_MethodOrCtorDeclaration getDsl_methodorctordeclaration() {
        return dsl_methodorctordeclaration;
    }

    public void setDsl_methodorctordeclaration(dsl_MethodOrCtorDeclaration dsl_methodorctordeclaration) {
        this.dsl_methodorctordeclaration = dsl_methodorctordeclaration;
    }
    public dsl_Initializer getDsl_initializer() {
        return dsl_initializer;
    }

    public void setDsl_initializer(dsl_Initializer dsl_initializer) {
        this.dsl_initializer = dsl_initializer;
    }

}