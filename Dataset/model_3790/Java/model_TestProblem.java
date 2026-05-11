





import java.util.List;
import java.util.ArrayList;

public class model_TestProblem  {

    private String message;
    private String problemType;





    private model_TestElement model_testelement;


    public model_TestProblem(
        String message,        String problemType    ) {
        this.message = message;
        this.problemType = problemType;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getProblemtype() {
        return problemType;
    }

    public void setProblemtype(String problemType) {
        this.problemType = problemType;
    }

    public model_TestElement getModel_testelement() {
        return model_testelement;
    }

    public void setModel_testelement(model_TestElement model_testelement) {
        this.model_testelement = model_testelement;
    }

}