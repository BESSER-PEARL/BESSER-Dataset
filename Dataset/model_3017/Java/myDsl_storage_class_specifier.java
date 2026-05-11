





import java.util.List;
import java.util.ArrayList;

public class myDsl_storage_class_specifier  {

    private String auto;
    private String thread_local;
    private String static;
    private String typedef;
    private String extern;
    private String register;



    public myDsl_storage_class_specifier(
        String auto,        String thread_local,        String static,        String typedef,        String extern,        String register    ) {
        this.auto = auto;
        this.thread_local = thread_local;
        this.static = static;
        this.typedef = typedef;
        this.extern = extern;
        this.register = register;
    }


    public String getAuto() {
        return auto;
    }

    public void setAuto(String auto) {
        this.auto = auto;
    }
    public String getThread_local() {
        return thread_local;
    }

    public void setThread_local(String thread_local) {
        this.thread_local = thread_local;
    }
    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }
    public String getTypedef() {
        return typedef;
    }

    public void setTypedef(String typedef) {
        this.typedef = typedef;
    }
    public String getExtern() {
        return extern;
    }

    public void setExtern(String extern) {
        this.extern = extern;
    }
    public String getRegister() {
        return register;
    }

    public void setRegister(String register) {
        this.register = register;
    }


}