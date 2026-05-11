





import java.util.List;
import java.util.ArrayList;

public class miniJava_State  {






    private miniJava_Program minijava_program;




    private miniJava_OutputStream minijava_outputstream;




    private miniJava_Frame minijava_frame;




    private miniJava_Frame minijava_frame;




    private miniJava_Context minijava_context;




    private List<miniJava_ArrayInstance> minijava_arrayinstances;




    private List<miniJava_ObjectInstance> minijava_objectinstances;


    public miniJava_State(
    ) {
        this.minijava_arrayinstances = new ArrayList<>();
        this.minijava_objectinstances = new ArrayList<>();
    }

    public miniJava_State(
        ArrayList<miniJava_ArrayInstance> minijava_arrayinstances,        ArrayList<miniJava_ObjectInstance> minijava_objectinstances    ) {
        this.minijava_arrayinstances = minijava_arrayinstances;
        this.minijava_objectinstances = minijava_objectinstances;
    }


    public miniJava_Program getMinijava_program() {
        return minijava_program;
    }

    public void setMinijava_program(miniJava_Program minijava_program) {
        this.minijava_program = minijava_program;
    }
    public miniJava_OutputStream getMinijava_outputstream() {
        return minijava_outputstream;
    }

    public void setMinijava_outputstream(miniJava_OutputStream minijava_outputstream) {
        this.minijava_outputstream = minijava_outputstream;
    }
    public miniJava_Frame getMinijava_frame() {
        return minijava_frame;
    }

    public void setMinijava_frame(miniJava_Frame minijava_frame) {
        this.minijava_frame = minijava_frame;
    }
    public miniJava_Frame getMinijava_frame() {
        return minijava_frame;
    }

    public void setMinijava_frame(miniJava_Frame minijava_frame) {
        this.minijava_frame = minijava_frame;
    }
    public miniJava_Context getMinijava_context() {
        return minijava_context;
    }

    public void setMinijava_context(miniJava_Context minijava_context) {
        this.minijava_context = minijava_context;
    }
    public List<miniJava_ArrayInstance> getMinijava_arrayinstances() {
        return minijava_arrayinstances;
    }

    public void addMinijava_arrayinstance(Minijava_arrayinstance minijava_arrayinstance) {
        this.minijava_arrayinstances.add(minijava_arrayinstance);
    }
    public List<miniJava_ObjectInstance> getMinijava_objectinstances() {
        return minijava_objectinstances;
    }

    public void addMinijava_objectinstance(Minijava_objectinstance minijava_objectinstance) {
        this.minijava_objectinstances.add(minijava_objectinstance);
    }

}