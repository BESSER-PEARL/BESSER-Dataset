





import java.util.List;
import java.util.ArrayList;

public class AsmL_AlgorithmSet extends SetTerm {






    private List<InWhereHolds> inwhereholdss;


    public AsmL_AlgorithmSet(
    ) {
        super(
        );
        this.inwhereholdss = new ArrayList<>();
    }

    public AsmL_AlgorithmSet(
        ArrayList<InWhereHolds> inwhereholdss    ) {
        this.inwhereholdss = inwhereholdss;
    }


    public List<InWhereHolds> getInwhereholdss() {
        return inwhereholdss;
    }

    public void addInwhereholds(Inwhereholds inwhereholds) {
        this.inwhereholdss.add(inwhereholds);
    }

}