





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ExecutableNode extends ActivityNode {






    private uml3_0_0_Clause uml3_0_0_clause;




    private uml3_0_0_LoopNode uml3_0_0_loopnode;




    private uml3_0_0_LoopNode uml3_0_0_loopnode;




    private uml3_0_0_LoopNode uml3_0_0_loopnode;




    private uml3_0_0_ExceptionHandler uml3_0_0_exceptionhandler;




    private List<uml3_0_0_ExceptionHandler> uml3_0_0_exceptionhandlers;




    private uml3_0_0_ExceptionHandler uml3_0_0_exceptionhandler;




    private uml3_0_0_Clause uml3_0_0_clause;


    public uml3_0_0_ExecutableNode(
    ) {
        super(
        );
        this.uml3_0_0_exceptionhandlers = new ArrayList<>();
    }

    public uml3_0_0_ExecutableNode(
        ArrayList<uml3_0_0_ExceptionHandler> uml3_0_0_exceptionhandlers    ) {
        this.uml3_0_0_exceptionhandlers = uml3_0_0_exceptionhandlers;
    }


    public uml3_0_0_Clause getUml3_0_0_clause() {
        return uml3_0_0_clause;
    }

    public void setUml3_0_0_clause(uml3_0_0_Clause uml3_0_0_clause) {
        this.uml3_0_0_clause = uml3_0_0_clause;
    }
    public uml3_0_0_LoopNode getUml3_0_0_loopnode() {
        return uml3_0_0_loopnode;
    }

    public void setUml3_0_0_loopnode(uml3_0_0_LoopNode uml3_0_0_loopnode) {
        this.uml3_0_0_loopnode = uml3_0_0_loopnode;
    }
    public uml3_0_0_LoopNode getUml3_0_0_loopnode() {
        return uml3_0_0_loopnode;
    }

    public void setUml3_0_0_loopnode(uml3_0_0_LoopNode uml3_0_0_loopnode) {
        this.uml3_0_0_loopnode = uml3_0_0_loopnode;
    }
    public uml3_0_0_LoopNode getUml3_0_0_loopnode() {
        return uml3_0_0_loopnode;
    }

    public void setUml3_0_0_loopnode(uml3_0_0_LoopNode uml3_0_0_loopnode) {
        this.uml3_0_0_loopnode = uml3_0_0_loopnode;
    }
    public uml3_0_0_ExceptionHandler getUml3_0_0_exceptionhandler() {
        return uml3_0_0_exceptionhandler;
    }

    public void setUml3_0_0_exceptionhandler(uml3_0_0_ExceptionHandler uml3_0_0_exceptionhandler) {
        this.uml3_0_0_exceptionhandler = uml3_0_0_exceptionhandler;
    }
    public List<uml3_0_0_ExceptionHandler> getUml3_0_0_exceptionhandlers() {
        return uml3_0_0_exceptionhandlers;
    }

    public void addUml3_0_0_exceptionhandler(Uml3_0_0_exceptionhandler uml3_0_0_exceptionhandler) {
        this.uml3_0_0_exceptionhandlers.add(uml3_0_0_exceptionhandler);
    }
    public uml3_0_0_ExceptionHandler getUml3_0_0_exceptionhandler() {
        return uml3_0_0_exceptionhandler;
    }

    public void setUml3_0_0_exceptionhandler(uml3_0_0_ExceptionHandler uml3_0_0_exceptionhandler) {
        this.uml3_0_0_exceptionhandler = uml3_0_0_exceptionhandler;
    }
    public uml3_0_0_Clause getUml3_0_0_clause() {
        return uml3_0_0_clause;
    }

    public void setUml3_0_0_clause(uml3_0_0_Clause uml3_0_0_clause) {
        this.uml3_0_0_clause = uml3_0_0_clause;
    }

}