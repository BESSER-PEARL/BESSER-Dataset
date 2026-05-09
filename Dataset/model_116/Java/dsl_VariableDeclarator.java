





import java.util.List;
import java.util.ArrayList;

public class dsl_VariableDeclarator  {






    private dsl_VariableInitializer dsl_variableinitializer;




    private dsl_FieldDeclaration dsl_fielddeclaration;


    public dsl_VariableDeclarator(
    ) {
    }



    public dsl_VariableInitializer getDsl_variableinitializer() {
        return dsl_variableinitializer;
    }

    public void setDsl_variableinitializer(dsl_VariableInitializer dsl_variableinitializer) {
        this.dsl_variableinitializer = dsl_variableinitializer;
    }
    public dsl_FieldDeclaration getDsl_fielddeclaration() {
        return dsl_fielddeclaration;
    }

    public void setDsl_fielddeclaration(dsl_FieldDeclaration dsl_fielddeclaration) {
        this.dsl_fielddeclaration = dsl_fielddeclaration;
    }

}