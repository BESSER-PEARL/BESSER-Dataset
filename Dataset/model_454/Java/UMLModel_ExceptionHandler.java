





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ExceptionHandler extends Element {

    private String protectedNode;
    private String handlerBody;
    private String exceptionType;
    private String exceptionInput;





    private UMLModel_ExecutableNode umlmodel_executablenode;


    public UMLModel_ExceptionHandler(
        String protectedNode,        String handlerBody,        String exceptionType,        String exceptionInput    ) {
        super(
        );
        this.protectedNode = protectedNode;
        this.handlerBody = handlerBody;
        this.exceptionType = exceptionType;
        this.exceptionInput = exceptionInput;
    }


    public String getProtectednode() {
        return protectedNode;
    }

    public void setProtectednode(String protectedNode) {
        this.protectedNode = protectedNode;
    }
    public String getHandlerbody() {
        return handlerBody;
    }

    public void setHandlerbody(String handlerBody) {
        this.handlerBody = handlerBody;
    }
    public String getExceptiontype() {
        return exceptionType;
    }

    public void setExceptiontype(String exceptionType) {
        this.exceptionType = exceptionType;
    }
    public String getExceptioninput() {
        return exceptionInput;
    }

    public void setExceptioninput(String exceptionInput) {
        this.exceptionInput = exceptionInput;
    }

    public UMLModel_ExecutableNode getUmlmodel_executablenode() {
        return umlmodel_executablenode;
    }

    public void setUmlmodel_executablenode(UMLModel_ExecutableNode umlmodel_executablenode) {
        this.umlmodel_executablenode = umlmodel_executablenode;
    }

}