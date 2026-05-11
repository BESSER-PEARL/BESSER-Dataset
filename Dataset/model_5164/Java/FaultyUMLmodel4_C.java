





import java.util.List;
import java.util.ArrayList;

public class FaultyUMLmodel4_C  {

    private int u;





    private List<FaultyUMLmodel4_B> faultyumlmodel4_bs;




    private FaultyUMLmodel4_B faultyumlmodel4_b;


    public FaultyUMLmodel4_C(
        int u    ) {
        this.u = u;
        this.faultyumlmodel4_bs = new ArrayList<>();
    }

    public FaultyUMLmodel4_C(
        int u        ArrayList<FaultyUMLmodel4_B> faultyumlmodel4_bs    ) {
        this.u = u;
        this.faultyumlmodel4_bs = faultyumlmodel4_bs;
    }

    public int getU() {
        return u;
    }

    public void setU(int u) {
        this.u = u;
    }

    public List<FaultyUMLmodel4_B> getFaultyumlmodel4_bs() {
        return faultyumlmodel4_bs;
    }

    public void addFaultyumlmodel4_b(Faultyumlmodel4_b faultyumlmodel4_b) {
        this.faultyumlmodel4_bs.add(faultyumlmodel4_b);
    }
    public FaultyUMLmodel4_B getFaultyumlmodel4_b() {
        return faultyumlmodel4_b;
    }

    public void setFaultyumlmodel4_b(FaultyUMLmodel4_B faultyumlmodel4_b) {
        this.faultyumlmodel4_b = faultyumlmodel4_b;
    }

}