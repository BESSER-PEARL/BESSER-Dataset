





import java.util.List;
import java.util.ArrayList;

public class FaultyRelations_A  {

    private int v;
    private boolean w;





    private FaultyRelations_B faultyrelations_b;




    private FaultyRelations_C faultyrelations_c;




    private List<FaultyRelations_B> faultyrelations_bs;




    private FaultyRelations_C faultyrelations_c;


    public FaultyRelations_A(
        int v,        boolean w    ) {
        this.v = v;
        this.w = w;
        this.faultyrelations_bs = new ArrayList<>();
    }

    public FaultyRelations_A(
        int v,        boolean w        ArrayList<FaultyRelations_B> faultyrelations_bs    ) {
        this.v = v;
        this.w = w;
        this.faultyrelations_bs = faultyrelations_bs;
    }

    public int getV() {
        return v;
    }

    public void setV(int v) {
        this.v = v;
    }
    public boolean getW() {
        return w;
    }

    public void setW(boolean w) {
        this.w = w;
    }

    public FaultyRelations_B getFaultyrelations_b() {
        return faultyrelations_b;
    }

    public void setFaultyrelations_b(FaultyRelations_B faultyrelations_b) {
        this.faultyrelations_b = faultyrelations_b;
    }
    public FaultyRelations_C getFaultyrelations_c() {
        return faultyrelations_c;
    }

    public void setFaultyrelations_c(FaultyRelations_C faultyrelations_c) {
        this.faultyrelations_c = faultyrelations_c;
    }
    public List<FaultyRelations_B> getFaultyrelations_bs() {
        return faultyrelations_bs;
    }

    public void addFaultyrelations_b(Faultyrelations_b faultyrelations_b) {
        this.faultyrelations_bs.add(faultyrelations_b);
    }
    public FaultyRelations_C getFaultyrelations_c() {
        return faultyrelations_c;
    }

    public void setFaultyrelations_c(FaultyRelations_C faultyrelations_c) {
        this.faultyrelations_c = faultyrelations_c;
    }

}