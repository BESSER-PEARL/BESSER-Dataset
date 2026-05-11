





import java.util.List;
import java.util.ArrayList;

public class SPL_SequenceConstant extends Constant {






    private List<SPL_Constant> spl_constants;


    public SPL_SequenceConstant(
    ) {
        super(
        );
        this.spl_constants = new ArrayList<>();
    }

    public SPL_SequenceConstant(
        ArrayList<SPL_Constant> spl_constants    ) {
        this.spl_constants = spl_constants;
    }


    public List<SPL_Constant> getSpl_constants() {
        return spl_constants;
    }

    public void addSpl_constant(Spl_constant spl_constant) {
        this.spl_constants.add(spl_constant);
    }

}