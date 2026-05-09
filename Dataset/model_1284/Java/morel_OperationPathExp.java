





import java.util.List;
import java.util.ArrayList;

public class morel_OperationPathExp extends CallPathExp {

    private String separator;
    private String operation;



    public morel_OperationPathExp(
        String separator,        String operation    ) {
        super(
        );
        this.separator = separator;
        this.operation = operation;
    }


    public String getSeparator() {
        return separator;
    }

    public void setSeparator(String separator) {
        this.separator = separator;
    }
    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }


}