





import java.util.List;
import java.util.ArrayList;

public class OCL_VariableDeclaration extends LocatedElement {

    private String varName;
    private String id;



    public OCL_VariableDeclaration(
        String varName,        String id    ) {
        super(
        );
        this.varName = varName;
        this.id = id;
    }


    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}