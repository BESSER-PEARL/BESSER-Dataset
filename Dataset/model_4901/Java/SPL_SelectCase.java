





import java.util.List;
import java.util.ArrayList;

public class SPL_SelectCase extends SelectMember {






    private List<SPL_Constant> spl_constants;




    private SPL_SelectStat spl_selectstat;


    public SPL_SelectCase(
    ) {
        super(
        );
        this.spl_constants = new ArrayList<>();
    }

    public SPL_SelectCase(
        ArrayList<SPL_Constant> spl_constants    ) {
        this.spl_constants = spl_constants;
    }


    public List<SPL_Constant> getSpl_constants() {
        return spl_constants;
    }

    public void addSpl_constant(Spl_constant spl_constant) {
        this.spl_constants.add(spl_constant);
    }
    public SPL_SelectStat getSpl_selectstat() {
        return spl_selectstat;
    }

    public void setSpl_selectstat(SPL_SelectStat spl_selectstat) {
        this.spl_selectstat = spl_selectstat;
    }

}