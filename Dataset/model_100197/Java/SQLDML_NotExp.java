





import java.util.List;
import java.util.ArrayList;

public class SQLDML_NotExp extends Expression {

    private String opName;



    public SQLDML_NotExp(
        String opName    ) {
        super(
        );
        this.opName = opName;
    }


    public String getOpname() {
        return opName;
    }

    public void setOpname(String opName) {
        this.opName = opName;
    }


}