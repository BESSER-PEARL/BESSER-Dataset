





import java.util.List;
import java.util.ArrayList;

public class FaultyUMLmodel4_D  {

    private boolean z;





    private List<FaultyUMLmodel4_C> faultyumlmodel4_cs;




    private FaultyUMLmodel4_C faultyumlmodel4_c;


    public FaultyUMLmodel4_D(
        boolean z    ) {
        this.z = z;
        this.faultyumlmodel4_cs = new ArrayList<>();
    }

    public FaultyUMLmodel4_D(
        boolean z        ArrayList<FaultyUMLmodel4_C> faultyumlmodel4_cs    ) {
        this.z = z;
        this.faultyumlmodel4_cs = faultyumlmodel4_cs;
    }

    public boolean getZ() {
        return z;
    }

    public void setZ(boolean z) {
        this.z = z;
    }

    public List<FaultyUMLmodel4_C> getFaultyumlmodel4_cs() {
        return faultyumlmodel4_cs;
    }

    public void addFaultyumlmodel4_c(Faultyumlmodel4_c faultyumlmodel4_c) {
        this.faultyumlmodel4_cs.add(faultyumlmodel4_c);
    }
    public FaultyUMLmodel4_C getFaultyumlmodel4_c() {
        return faultyumlmodel4_c;
    }

    public void setFaultyumlmodel4_c(FaultyUMLmodel4_C faultyumlmodel4_c) {
        this.faultyumlmodel4_c = faultyumlmodel4_c;
    }

}