





import java.util.List;
import java.util.ArrayList;

public class FaultyRelations_C  {

    private int u;





    private FaultyRelations_B faultyrelations_b;




    private List<FaultyRelations_B> faultyrelations_bs;


    public FaultyRelations_C(
        int u    ) {
        this.u = u;
        this.faultyrelations_bs = new ArrayList<>();
    }

    public FaultyRelations_C(
        int u        ArrayList<FaultyRelations_B> faultyrelations_bs    ) {
        this.u = u;
        this.faultyrelations_bs = faultyrelations_bs;
    }

    public int getU() {
        return u;
    }

    public void setU(int u) {
        this.u = u;
    }

    public FaultyRelations_B getFaultyrelations_b() {
        return faultyrelations_b;
    }

    public void setFaultyrelations_b(FaultyRelations_B faultyrelations_b) {
        this.faultyrelations_b = faultyrelations_b;
    }
    public List<FaultyRelations_B> getFaultyrelations_bs() {
        return faultyrelations_bs;
    }

    public void addFaultyrelations_b(Faultyrelations_b faultyrelations_b) {
        this.faultyrelations_bs.add(faultyrelations_b);
    }

}