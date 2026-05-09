





import java.util.List;
import java.util.ArrayList;

public class graph_NodeResponsibility extends Identifiable {

    private String operation;



    public graph_NodeResponsibility(
        String operation    ) {
        super(
        );
        this.operation = operation;
    }


    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }


}