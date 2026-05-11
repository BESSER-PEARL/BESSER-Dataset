





import java.util.List;
import java.util.ArrayList;

public class jcl_statements_ExecuteProcedure extends Execute {

    private String procedureName;



    public jcl_statements_ExecuteProcedure(
        String procedureName    ) {
        super(
        );
        this.procedureName = procedureName;
    }


    public String getProcedurename() {
        return procedureName;
    }

    public void setProcedurename(String procedureName) {
        this.procedureName = procedureName;
    }


}