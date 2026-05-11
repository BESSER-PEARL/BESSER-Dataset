





import java.util.List;
import java.util.ArrayList;

public class SPL_FunctionDeclaration extends Declaration {






    private List<SPL_Argument> spl_arguments;




    private SPL_FunctionCall spl_functioncall;




    private SPL_TypeExpression spl_typeexpression;


    public SPL_FunctionDeclaration(
    ) {
        super(
        );
        this.spl_arguments = new ArrayList<>();
    }

    public SPL_FunctionDeclaration(
        ArrayList<SPL_Argument> spl_arguments    ) {
        this.spl_arguments = spl_arguments;
    }


    public List<SPL_Argument> getSpl_arguments() {
        return spl_arguments;
    }

    public void addSpl_argument(Spl_argument spl_argument) {
        this.spl_arguments.add(spl_argument);
    }
    public SPL_FunctionCall getSpl_functioncall() {
        return spl_functioncall;
    }

    public void setSpl_functioncall(SPL_FunctionCall spl_functioncall) {
        this.spl_functioncall = spl_functioncall;
    }
    public SPL_TypeExpression getSpl_typeexpression() {
        return spl_typeexpression;
    }

    public void setSpl_typeexpression(SPL_TypeExpression spl_typeexpression) {
        this.spl_typeexpression = spl_typeexpression;
    }

}