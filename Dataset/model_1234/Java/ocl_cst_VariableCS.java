





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_VariableCS extends CSTNode {

    private String name;



    public ocl_cst_VariableCS(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}