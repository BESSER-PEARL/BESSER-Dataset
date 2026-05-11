





import java.util.List;
import java.util.ArrayList;

public class gx10_Method  {

    private String name;





    private gx10_Program gx10_program;




    private gx10_Program gx10_program;




    private gx10_MethodCall gx10_methodcall;




    private List<gx10_MethodCall> gx10_methodcalls;




    private gx10_Program gx10_program;




    private gx10_Block gx10_block;




    private List<gx10_Referentiable> gx10_referentiables;


    public gx10_Method(
        String name    ) {
        this.name = name;
        this.gx10_methodcalls = new ArrayList<>();
        this.gx10_referentiables = new ArrayList<>();
    }

    public gx10_Method(
        String name        ArrayList<gx10_MethodCall> gx10_methodcalls,        ArrayList<gx10_Referentiable> gx10_referentiables    ) {
        this.name = name;
        this.gx10_methodcalls = gx10_methodcalls;
        this.gx10_referentiables = gx10_referentiables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gx10_Program getGx10_program() {
        return gx10_program;
    }

    public void setGx10_program(gx10_Program gx10_program) {
        this.gx10_program = gx10_program;
    }
    public gx10_Program getGx10_program() {
        return gx10_program;
    }

    public void setGx10_program(gx10_Program gx10_program) {
        this.gx10_program = gx10_program;
    }
    public gx10_MethodCall getGx10_methodcall() {
        return gx10_methodcall;
    }

    public void setGx10_methodcall(gx10_MethodCall gx10_methodcall) {
        this.gx10_methodcall = gx10_methodcall;
    }
    public List<gx10_MethodCall> getGx10_methodcalls() {
        return gx10_methodcalls;
    }

    public void addGx10_methodcall(Gx10_methodcall gx10_methodcall) {
        this.gx10_methodcalls.add(gx10_methodcall);
    }
    public gx10_Program getGx10_program() {
        return gx10_program;
    }

    public void setGx10_program(gx10_Program gx10_program) {
        this.gx10_program = gx10_program;
    }
    public gx10_Block getGx10_block() {
        return gx10_block;
    }

    public void setGx10_block(gx10_Block gx10_block) {
        this.gx10_block = gx10_block;
    }
    public List<gx10_Referentiable> getGx10_referentiables() {
        return gx10_referentiables;
    }

    public void addGx10_referentiable(Gx10_referentiable gx10_referentiable) {
        this.gx10_referentiables.add(gx10_referentiable);
    }

}