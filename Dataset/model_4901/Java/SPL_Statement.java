





import java.util.List;
import java.util.ArrayList;

public class SPL_Statement extends LocatedElement {






    private SPL_Branch spl_branch;


    public SPL_Statement(
    ) {
        super(
        );
    }



    public SPL_Branch getSpl_branch() {
        return spl_branch;
    }

    public void setSpl_branch(SPL_Branch spl_branch) {
        this.spl_branch = spl_branch;
    }

}