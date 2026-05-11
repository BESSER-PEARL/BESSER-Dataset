





import java.util.List;
import java.util.ArrayList;

public class gDSL_Args  {






    private gDSL_ApplyExp gdsl_applyexp;




    private List<gDSL_AtomicExp> gdsl_atomicexps;


    public gDSL_Args(
    ) {
        this.gdsl_atomicexps = new ArrayList<>();
    }

    public gDSL_Args(
        ArrayList<gDSL_AtomicExp> gdsl_atomicexps    ) {
        this.gdsl_atomicexps = gdsl_atomicexps;
    }


    public gDSL_ApplyExp getGdsl_applyexp() {
        return gdsl_applyexp;
    }

    public void setGdsl_applyexp(gDSL_ApplyExp gdsl_applyexp) {
        this.gdsl_applyexp = gdsl_applyexp;
    }
    public List<gDSL_AtomicExp> getGdsl_atomicexps() {
        return gdsl_atomicexps;
    }

    public void addGdsl_atomicexp(Gdsl_atomicexp gdsl_atomicexp) {
        this.gdsl_atomicexps.add(gdsl_atomicexp);
    }

}