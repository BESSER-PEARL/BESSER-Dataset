





import java.util.List;
import java.util.ArrayList;

public class ref_unsettable_CU  {






    private List<DU> dus;


    public ref_unsettable_CU(
    ) {
        this.dus = new ArrayList<>();
    }

    public ref_unsettable_CU(
        ArrayList<DU> dus    ) {
        this.dus = dus;
    }


    public List<DU> getDus() {
        return dus;
    }

    public void addDu(Du du) {
        this.dus.add(du);
    }

}