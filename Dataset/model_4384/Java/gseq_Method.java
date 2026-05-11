





import java.util.List;
import java.util.ArrayList;

public class gseq_Method  {

    private String name;





    private List<gseq_Operation> gseq_operations;




    private gseq_Program gseq_program;




    private gseq_Program gseq_program;




    private gseq_Program gseq_program;




    private gseq_Operation gseq_operation;




    private List<gseq_MethodCall> gseq_methodcalls;




    private gseq_MethodCall gseq_methodcall;


    public gseq_Method(
        String name    ) {
        this.name = name;
        this.gseq_operations = new ArrayList<>();
        this.gseq_methodcalls = new ArrayList<>();
    }

    public gseq_Method(
        String name        ArrayList<gseq_Operation> gseq_operations,        ArrayList<gseq_MethodCall> gseq_methodcalls    ) {
        this.name = name;
        this.gseq_operations = gseq_operations;
        this.gseq_methodcalls = gseq_methodcalls;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<gseq_Operation> getGseq_operations() {
        return gseq_operations;
    }

    public void addGseq_operation(Gseq_operation gseq_operation) {
        this.gseq_operations.add(gseq_operation);
    }
    public gseq_Program getGseq_program() {
        return gseq_program;
    }

    public void setGseq_program(gseq_Program gseq_program) {
        this.gseq_program = gseq_program;
    }
    public gseq_Program getGseq_program() {
        return gseq_program;
    }

    public void setGseq_program(gseq_Program gseq_program) {
        this.gseq_program = gseq_program;
    }
    public gseq_Program getGseq_program() {
        return gseq_program;
    }

    public void setGseq_program(gseq_Program gseq_program) {
        this.gseq_program = gseq_program;
    }
    public gseq_Operation getGseq_operation() {
        return gseq_operation;
    }

    public void setGseq_operation(gseq_Operation gseq_operation) {
        this.gseq_operation = gseq_operation;
    }
    public List<gseq_MethodCall> getGseq_methodcalls() {
        return gseq_methodcalls;
    }

    public void addGseq_methodcall(Gseq_methodcall gseq_methodcall) {
        this.gseq_methodcalls.add(gseq_methodcall);
    }
    public gseq_MethodCall getGseq_methodcall() {
        return gseq_methodcall;
    }

    public void setGseq_methodcall(gseq_MethodCall gseq_methodcall) {
        this.gseq_methodcall = gseq_methodcall;
    }

}