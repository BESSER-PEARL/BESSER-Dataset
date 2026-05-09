





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ExecutableNode extends ActivityNode {






    private UML2WithID_ExceptionHandler uml2withid_exceptionhandler;




    private List<UML2WithID_ExceptionHandler> uml2withid_exceptionhandlers;




    private UML2WithID_ExceptionHandler uml2withid_exceptionhandler;


    public UML2WithID_ExecutableNode(
    ) {
        super(
        );
        this.uml2withid_exceptionhandlers = new ArrayList<>();
    }

    public UML2WithID_ExecutableNode(
        ArrayList<UML2WithID_ExceptionHandler> uml2withid_exceptionhandlers    ) {
        this.uml2withid_exceptionhandlers = uml2withid_exceptionhandlers;
    }


    public UML2WithID_ExceptionHandler getUml2withid_exceptionhandler() {
        return uml2withid_exceptionhandler;
    }

    public void setUml2withid_exceptionhandler(UML2WithID_ExceptionHandler uml2withid_exceptionhandler) {
        this.uml2withid_exceptionhandler = uml2withid_exceptionhandler;
    }
    public List<UML2WithID_ExceptionHandler> getUml2withid_exceptionhandlers() {
        return uml2withid_exceptionhandlers;
    }

    public void addUml2withid_exceptionhandler(Uml2withid_exceptionhandler uml2withid_exceptionhandler) {
        this.uml2withid_exceptionhandlers.add(uml2withid_exceptionhandler);
    }
    public UML2WithID_ExceptionHandler getUml2withid_exceptionhandler() {
        return uml2withid_exceptionhandler;
    }

    public void setUml2withid_exceptionhandler(UML2WithID_ExceptionHandler uml2withid_exceptionhandler) {
        this.uml2withid_exceptionhandler = uml2withid_exceptionhandler;
    }

}