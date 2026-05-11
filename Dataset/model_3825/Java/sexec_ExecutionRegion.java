





import java.util.List;
import java.util.ArrayList;

public class sexec_ExecutionRegion extends ExecutionScope {






    private List<sexec_ExecutionNode> sexec_executionnodes;


    public sexec_ExecutionRegion(
    ) {
        super(
        );
        this.sexec_executionnodes = new ArrayList<>();
    }

    public sexec_ExecutionRegion(
        ArrayList<sexec_ExecutionNode> sexec_executionnodes    ) {
        this.sexec_executionnodes = sexec_executionnodes;
    }


    public List<sexec_ExecutionNode> getSexec_executionnodes() {
        return sexec_executionnodes;
    }

    public void addSexec_executionnode(Sexec_executionnode sexec_executionnode) {
        this.sexec_executionnodes.add(sexec_executionnode);
    }

}