





import java.util.List;
import java.util.ArrayList;

public class FaultyUMLmodel4_A  {

    private boolean w;
    private int v;





    private FaultyUMLmodel4_B faultyumlmodel4_b;




    private FaultyUMLmodel4_C faultyumlmodel4_c;




    private FaultyUMLmodel4_C faultyumlmodel4_c;




    private List<FaultyUMLmodel4_B> faultyumlmodel4_bs;


    public FaultyUMLmodel4_A(
        boolean w,        int v    ) {
        this.w = w;
        this.v = v;
        this.faultyumlmodel4_bs = new ArrayList<>();
    }

    public FaultyUMLmodel4_A(
        boolean w,        int v        ArrayList<FaultyUMLmodel4_B> faultyumlmodel4_bs    ) {
        this.w = w;
        this.v = v;
        this.faultyumlmodel4_bs = faultyumlmodel4_bs;
    }

    public boolean getW() {
        return w;
    }

    public void setW(boolean w) {
        this.w = w;
    }
    public int getV() {
        return v;
    }

    public void setV(int v) {
        this.v = v;
    }

    public FaultyUMLmodel4_B getFaultyumlmodel4_b() {
        return faultyumlmodel4_b;
    }

    public void setFaultyumlmodel4_b(FaultyUMLmodel4_B faultyumlmodel4_b) {
        this.faultyumlmodel4_b = faultyumlmodel4_b;
    }
    public FaultyUMLmodel4_C getFaultyumlmodel4_c() {
        return faultyumlmodel4_c;
    }

    public void setFaultyumlmodel4_c(FaultyUMLmodel4_C faultyumlmodel4_c) {
        this.faultyumlmodel4_c = faultyumlmodel4_c;
    }
    public FaultyUMLmodel4_C getFaultyumlmodel4_c() {
        return faultyumlmodel4_c;
    }

    public void setFaultyumlmodel4_c(FaultyUMLmodel4_C faultyumlmodel4_c) {
        this.faultyumlmodel4_c = faultyumlmodel4_c;
    }
    public List<FaultyUMLmodel4_B> getFaultyumlmodel4_bs() {
        return faultyumlmodel4_bs;
    }

    public void addFaultyumlmodel4_b(Faultyumlmodel4_b faultyumlmodel4_b) {
        this.faultyumlmodel4_bs.add(faultyumlmodel4_b);
    }

}