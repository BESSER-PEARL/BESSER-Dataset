





import java.util.List;
import java.util.ArrayList;

public class UML2_ExecutableNode extends ActivityNode {






    private List<UML2_ExceptionHandler> uml2_exceptionhandlers;




    private UML2_ExceptionHandler uml2_exceptionhandler;




    private UML2_ExceptionHandler uml2_exceptionhandler;


    public UML2_ExecutableNode(
    ) {
        super(
        );
        this.uml2_exceptionhandlers = new ArrayList<>();
    }

    public UML2_ExecutableNode(
        ArrayList<UML2_ExceptionHandler> uml2_exceptionhandlers    ) {
        this.uml2_exceptionhandlers = uml2_exceptionhandlers;
    }


    public List<UML2_ExceptionHandler> getUml2_exceptionhandlers() {
        return uml2_exceptionhandlers;
    }

    public void addUml2_exceptionhandler(Uml2_exceptionhandler uml2_exceptionhandler) {
        this.uml2_exceptionhandlers.add(uml2_exceptionhandler);
    }
    public UML2_ExceptionHandler getUml2_exceptionhandler() {
        return uml2_exceptionhandler;
    }

    public void setUml2_exceptionhandler(UML2_ExceptionHandler uml2_exceptionhandler) {
        this.uml2_exceptionhandler = uml2_exceptionhandler;
    }
    public UML2_ExceptionHandler getUml2_exceptionhandler() {
        return uml2_exceptionhandler;
    }

    public void setUml2_exceptionhandler(UML2_ExceptionHandler uml2_exceptionhandler) {
        this.uml2_exceptionhandler = uml2_exceptionhandler;
    }

}