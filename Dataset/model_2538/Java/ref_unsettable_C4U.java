





import java.util.List;
import java.util.ArrayList;

public class ref_unsettable_C4U  {






    private CU cu;




    private List<DU> dus;


    public ref_unsettable_C4U(
    ) {
        this.dus = new ArrayList<>();
    }

    public ref_unsettable_C4U(
        ArrayList<DU> dus    ) {
        this.dus = dus;
    }


    public CU getCu() {
        return cu;
    }

    public void setCu(CU cu) {
        this.cu = cu;
    }
    public List<DU> getDus() {
        return dus;
    }

    public void addDu(Du du) {
        this.dus.add(du);
    }

}