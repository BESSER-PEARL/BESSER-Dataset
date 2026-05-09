





import java.util.List;
import java.util.ArrayList;

public class uml_ExecutableNode extends ActivityNode {






    private uml_ExceptionHandler uml_exceptionhandler;




    private List<uml_ExceptionHandler> uml_exceptionhandlers;




    private uml_Clause uml_clause;




    private uml_ExceptionHandler uml_exceptionhandler;




    private uml_Clause uml_clause;


    public uml_ExecutableNode(
    ) {
        super(
        );
        this.uml_exceptionhandlers = new ArrayList<>();
    }

    public uml_ExecutableNode(
        ArrayList<uml_ExceptionHandler> uml_exceptionhandlers    ) {
        this.uml_exceptionhandlers = uml_exceptionhandlers;
    }


    public uml_ExceptionHandler getUml_exceptionhandler() {
        return uml_exceptionhandler;
    }

    public void setUml_exceptionhandler(uml_ExceptionHandler uml_exceptionhandler) {
        this.uml_exceptionhandler = uml_exceptionhandler;
    }
    public List<uml_ExceptionHandler> getUml_exceptionhandlers() {
        return uml_exceptionhandlers;
    }

    public void addUml_exceptionhandler(Uml_exceptionhandler uml_exceptionhandler) {
        this.uml_exceptionhandlers.add(uml_exceptionhandler);
    }
    public uml_Clause getUml_clause() {
        return uml_clause;
    }

    public void setUml_clause(uml_Clause uml_clause) {
        this.uml_clause = uml_clause;
    }
    public uml_ExceptionHandler getUml_exceptionhandler() {
        return uml_exceptionhandler;
    }

    public void setUml_exceptionhandler(uml_ExceptionHandler uml_exceptionhandler) {
        this.uml_exceptionhandler = uml_exceptionhandler;
    }
    public uml_Clause getUml_clause() {
        return uml_clause;
    }

    public void setUml_clause(uml_Clause uml_clause) {
        this.uml_clause = uml_clause;
    }

}