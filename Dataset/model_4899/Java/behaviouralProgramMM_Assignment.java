





import java.util.List;
import java.util.ArrayList;

public class behaviouralProgramMM_Assignment extends Statement {

    private String VariableName;



    public behaviouralProgramMM_Assignment(
        String VariableName    ) {
        super(
        );
        this.VariableName = VariableName;
    }


    public String getVariablename() {
        return VariableName;
    }

    public void setVariablename(String VariableName) {
        this.VariableName = VariableName;
    }


}