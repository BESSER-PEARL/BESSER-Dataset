





import java.util.List;
import java.util.ArrayList;

public class AsmL_PredicateTerm extends Term {






    private List<InWhereHolds> inwhereholdss;


    public AsmL_PredicateTerm(
    ) {
        super(
        );
        this.inwhereholdss = new ArrayList<>();
    }

    public AsmL_PredicateTerm(
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