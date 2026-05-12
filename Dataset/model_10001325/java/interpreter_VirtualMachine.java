





import java.util.List;
import java.util.ArrayList;

public class interpreter_VirtualMachine  {

    private boolean dumpState;
    private boolean isRunning;
    private int returnAddrs;
    private int pc;





    private interpreter_Program interpreter_program;




    private interpreter_RunTimeStack interpreter_runtimestack;


    public interpreter_VirtualMachine(
        boolean dumpState,        boolean isRunning,        int returnAddrs,        int pc    ) {
        this.dumpState = dumpState;
        this.isRunning = isRunning;
        this.returnAddrs = returnAddrs;
        this.pc = pc;
    }


    public boolean getDumpstate() {
        return dumpState;
    }

    public void setDumpstate(boolean dumpState) {
        this.dumpState = dumpState;
    }
    public boolean getIsrunning() {
        return isRunning;
    }

    public void setIsrunning(boolean isRunning) {
        this.isRunning = isRunning;
    }
    public int getReturnaddrs() {
        return returnAddrs;
    }

    public void setReturnaddrs(int returnAddrs) {
        this.returnAddrs = returnAddrs;
    }
    public int getPc() {
        return pc;
    }

    public void setPc(int pc) {
        this.pc = pc;
    }

    public interpreter_Program getInterpreter_program() {
        return interpreter_program;
    }

    public void setInterpreter_program(interpreter_Program interpreter_program) {
        this.interpreter_program = interpreter_program;
    }
    public interpreter_RunTimeStack getInterpreter_runtimestack() {
        return interpreter_runtimestack;
    }

    public void setInterpreter_runtimestack(interpreter_RunTimeStack interpreter_runtimestack) {
        this.interpreter_runtimestack = interpreter_runtimestack;
    }

}