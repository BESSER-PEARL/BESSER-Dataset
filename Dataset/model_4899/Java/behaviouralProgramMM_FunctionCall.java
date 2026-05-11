





import java.util.List;
import java.util.ArrayList;

public class behaviouralProgramMM_FunctionCall extends Expression {

    private String FuncName;





    private List<behaviouralProgramMM_Expression> behaviouralprogrammm_expressions;


    public behaviouralProgramMM_FunctionCall(
        String FuncName    ) {
        super(
        );
        this.FuncName = FuncName;
        this.behaviouralprogrammm_expressions = new ArrayList<>();
    }

    public behaviouralProgramMM_FunctionCall(
        String FuncName        ArrayList<behaviouralProgramMM_Expression> behaviouralprogrammm_expressions    ) {
        this.FuncName = FuncName;
        this.behaviouralprogrammm_expressions = behaviouralprogrammm_expressions;
    }

    public String getFuncname() {
        return FuncName;
    }

    public void setFuncname(String FuncName) {
        this.FuncName = FuncName;
    }

    public List<behaviouralProgramMM_Expression> getBehaviouralprogrammm_expressions() {
        return behaviouralprogrammm_expressions;
    }

    public void addBehaviouralprogrammm_expression(Behaviouralprogrammm_expression behaviouralprogrammm_expression) {
        this.behaviouralprogrammm_expressions.add(behaviouralprogrammm_expression);
    }

}