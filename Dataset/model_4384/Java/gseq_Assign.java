





import java.util.List;
import java.util.ArrayList;

public class gseq_Assign extends Operation {

    private String varName;



    public gseq_Assign(
        String varName    ) {
        super(
        );
        this.varName = varName;
    }


    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }


}