





import java.util.List;
import java.util.ArrayList;

public class simpleimperative_Expression  {






    private simpleimperative_Assignation simpleimperative_assignation;




    private simpleimperative_VarDecl simpleimperative_vardecl;




    private simpleimperative_Conditional simpleimperative_conditional;




    private simpleimperative_Loop simpleimperative_loop;


    public simpleimperative_Expression(
    ) {
    }



    public simpleimperative_Assignation getSimpleimperative_assignation() {
        return simpleimperative_assignation;
    }

    public void setSimpleimperative_assignation(simpleimperative_Assignation simpleimperative_assignation) {
        this.simpleimperative_assignation = simpleimperative_assignation;
    }
    public simpleimperative_VarDecl getSimpleimperative_vardecl() {
        return simpleimperative_vardecl;
    }

    public void setSimpleimperative_vardecl(simpleimperative_VarDecl simpleimperative_vardecl) {
        this.simpleimperative_vardecl = simpleimperative_vardecl;
    }
    public simpleimperative_Conditional getSimpleimperative_conditional() {
        return simpleimperative_conditional;
    }

    public void setSimpleimperative_conditional(simpleimperative_Conditional simpleimperative_conditional) {
        this.simpleimperative_conditional = simpleimperative_conditional;
    }
    public simpleimperative_Loop getSimpleimperative_loop() {
        return simpleimperative_loop;
    }

    public void setSimpleimperative_loop(simpleimperative_Loop simpleimperative_loop) {
        this.simpleimperative_loop = simpleimperative_loop;
    }

}