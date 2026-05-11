





import java.util.List;
import java.util.ArrayList;

public class ir_TimeLoop extends IrAnnotable {

    private String name;





    private ir_Expression ir_expression;




    private List<ir_TimeLoopVariable> ir_timeloopvariables;




    private ir_TimeLoop ir_timeloop;




    private ir_TimeLoop ir_timeloop;


    public ir_TimeLoop(
        String name    ) {
        super(
        );
        this.name = name;
        this.ir_timeloopvariables = new ArrayList<>();
    }

    public ir_TimeLoop(
        String name        ArrayList<ir_TimeLoopVariable> ir_timeloopvariables    ) {
        this.name = name;
        this.ir_timeloopvariables = ir_timeloopvariables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ir_Expression getIr_expression() {
        return ir_expression;
    }

    public void setIr_expression(ir_Expression ir_expression) {
        this.ir_expression = ir_expression;
    }
    public List<ir_TimeLoopVariable> getIr_timeloopvariables() {
        return ir_timeloopvariables;
    }

    public void addIr_timeloopvariable(Ir_timeloopvariable ir_timeloopvariable) {
        this.ir_timeloopvariables.add(ir_timeloopvariable);
    }
    public ir_TimeLoop getIr_timeloop() {
        return ir_timeloop;
    }

    public void setIr_timeloop(ir_TimeLoop ir_timeloop) {
        this.ir_timeloop = ir_timeloop;
    }
    public ir_TimeLoop getIr_timeloop() {
        return ir_timeloop;
    }

    public void setIr_timeloop(ir_TimeLoop ir_timeloop) {
        this.ir_timeloop = ir_timeloop;
    }

}