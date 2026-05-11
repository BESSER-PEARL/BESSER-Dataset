





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedExecutableNode extends TracedActivityNode {






    private List<uml_TracedExceptionHandler> uml_tracedexceptionhandlers;


    public umlTrace_uml_TracedExecutableNode(
    ) {
        super(
        );
        this.uml_tracedexceptionhandlers = new ArrayList<>();
    }

    public umlTrace_uml_TracedExecutableNode(
        ArrayList<uml_TracedExceptionHandler> uml_tracedexceptionhandlers    ) {
        this.uml_tracedexceptionhandlers = uml_tracedexceptionhandlers;
    }


    public List<uml_TracedExceptionHandler> getUml_tracedexceptionhandlers() {
        return uml_tracedexceptionhandlers;
    }

    public void addUml_tracedexceptionhandler(Uml_tracedexceptionhandler uml_tracedexceptionhandler) {
        this.uml_tracedexceptionhandlers.add(uml_tracedexceptionhandler);
    }

}