





import java.util.List;
import java.util.ArrayList;

public class dbl_Parameter extends AbstractVariable {






    private dbl_Constructor dbl_constructor;




    private dbl_Procedure dbl_procedure;




    private dbl_Pattern dbl_pattern;


    public dbl_Parameter(
    ) {
        super(
        );
    }



    public dbl_Constructor getDbl_constructor() {
        return dbl_constructor;
    }

    public void setDbl_constructor(dbl_Constructor dbl_constructor) {
        this.dbl_constructor = dbl_constructor;
    }
    public dbl_Procedure getDbl_procedure() {
        return dbl_procedure;
    }

    public void setDbl_procedure(dbl_Procedure dbl_procedure) {
        this.dbl_procedure = dbl_procedure;
    }
    public dbl_Pattern getDbl_pattern() {
        return dbl_pattern;
    }

    public void setDbl_pattern(dbl_Pattern dbl_pattern) {
        this.dbl_pattern = dbl_pattern;
    }

}