





import java.util.List;
import java.util.ArrayList;

public class ref_unsettable_C3U  {






    private List<DU> dus;




    private CU cu;


    public ref_unsettable_C3U(
    ) {
        this.dus = new ArrayList<>();
    }

    public ref_unsettable_C3U(
        ArrayList<DU> dus    ) {
        this.dus = dus;
    }


    public List<DU> getDus() {
        return dus;
    }

    public void addDu(Du du) {
        this.dus.add(du);
    }
    public CU getCu() {
        return cu;
    }

    public void setCu(CU cu) {
        this.cu = cu;
    }

}