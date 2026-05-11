





import java.util.List;
import java.util.ArrayList;

public class miniJava_ObjectInstance  {






    private List<miniJava_FieldBinding> minijava_fieldbindings;




    private miniJava_ObjectRefValue minijava_objectrefvalue;




    private miniJava_Frame minijava_frame;


    public miniJava_ObjectInstance(
    ) {
        this.minijava_fieldbindings = new ArrayList<>();
    }

    public miniJava_ObjectInstance(
        ArrayList<miniJava_FieldBinding> minijava_fieldbindings    ) {
        this.minijava_fieldbindings = minijava_fieldbindings;
    }


    public List<miniJava_FieldBinding> getMinijava_fieldbindings() {
        return minijava_fieldbindings;
    }

    public void addMinijava_fieldbinding(Minijava_fieldbinding minijava_fieldbinding) {
        this.minijava_fieldbindings.add(minijava_fieldbinding);
    }
    public miniJava_ObjectRefValue getMinijava_objectrefvalue() {
        return minijava_objectrefvalue;
    }

    public void setMinijava_objectrefvalue(miniJava_ObjectRefValue minijava_objectrefvalue) {
        this.minijava_objectrefvalue = minijava_objectrefvalue;
    }
    public miniJava_Frame getMinijava_frame() {
        return minijava_frame;
    }

    public void setMinijava_frame(miniJava_Frame minijava_frame) {
        this.minijava_frame = minijava_frame;
    }

}