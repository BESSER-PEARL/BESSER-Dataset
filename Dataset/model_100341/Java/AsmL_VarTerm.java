





import java.util.List;
import java.util.ArrayList;

public class AsmL_VarTerm extends Term {

    private String name;



    public AsmL_VarTerm(
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