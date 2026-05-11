





import java.util.List;
import java.util.ArrayList;

public class ir_Variable extends ArgOrVar {

    private boolean const;
    private String persistenceName;





    private ir_TimeLoopCopy ir_timeloopcopy;




    private ir_TimeLoopVariable ir_timeloopvariable;




    private ir_TimeLoopVariable ir_timeloopvariable;




    private ir_TimeLoopCopy ir_timeloopcopy;




    private ir_TimeLoopVariable ir_timeloopvariable;




    private ir_PostProcessingInfo ir_postprocessinginfo;


    public ir_Variable(
        boolean const,        String persistenceName    ) {
        super(
        );
        this.const = const;
        this.persistenceName = persistenceName;
    }


    public boolean getConst() {
        return const;
    }

    public void setConst(boolean const) {
        this.const = const;
    }
    public String getPersistencename() {
        return persistenceName;
    }

    public void setPersistencename(String persistenceName) {
        this.persistenceName = persistenceName;
    }

    public ir_TimeLoopCopy getIr_timeloopcopy() {
        return ir_timeloopcopy;
    }

    public void setIr_timeloopcopy(ir_TimeLoopCopy ir_timeloopcopy) {
        this.ir_timeloopcopy = ir_timeloopcopy;
    }
    public ir_TimeLoopVariable getIr_timeloopvariable() {
        return ir_timeloopvariable;
    }

    public void setIr_timeloopvariable(ir_TimeLoopVariable ir_timeloopvariable) {
        this.ir_timeloopvariable = ir_timeloopvariable;
    }
    public ir_TimeLoopVariable getIr_timeloopvariable() {
        return ir_timeloopvariable;
    }

    public void setIr_timeloopvariable(ir_TimeLoopVariable ir_timeloopvariable) {
        this.ir_timeloopvariable = ir_timeloopvariable;
    }
    public ir_TimeLoopCopy getIr_timeloopcopy() {
        return ir_timeloopcopy;
    }

    public void setIr_timeloopcopy(ir_TimeLoopCopy ir_timeloopcopy) {
        this.ir_timeloopcopy = ir_timeloopcopy;
    }
    public ir_TimeLoopVariable getIr_timeloopvariable() {
        return ir_timeloopvariable;
    }

    public void setIr_timeloopvariable(ir_TimeLoopVariable ir_timeloopvariable) {
        this.ir_timeloopvariable = ir_timeloopvariable;
    }
    public ir_PostProcessingInfo getIr_postprocessinginfo() {
        return ir_postprocessinginfo;
    }

    public void setIr_postprocessinginfo(ir_PostProcessingInfo ir_postprocessinginfo) {
        this.ir_postprocessinginfo = ir_postprocessinginfo;
    }

}