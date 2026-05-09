





import java.util.List;
import java.util.ArrayList;

public class pDL2_WorkDefinition extends ProcessElement {

    private String name;





    private List<pDL2_DependanceStart> pdl2_dependancestarts;




    private List<pDL2_DependanceFinish> pdl2_dependancefinishs;




    private pDL2_DependanceStart pdl2_dependancestart;




    private pDL2_DependanceFinish pdl2_dependancefinish;


    public pDL2_WorkDefinition(
        String name    ) {
        super(
        );
        this.name = name;
        this.pdl2_dependancestarts = new ArrayList<>();
        this.pdl2_dependancefinishs = new ArrayList<>();
    }

    public pDL2_WorkDefinition(
        String name        ArrayList<pDL2_DependanceStart> pdl2_dependancestarts,        ArrayList<pDL2_DependanceFinish> pdl2_dependancefinishs    ) {
        this.name = name;
        this.pdl2_dependancestarts = pdl2_dependancestarts;
        this.pdl2_dependancefinishs = pdl2_dependancefinishs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<pDL2_DependanceStart> getPdl2_dependancestarts() {
        return pdl2_dependancestarts;
    }

    public void addPdl2_dependancestart(Pdl2_dependancestart pdl2_dependancestart) {
        this.pdl2_dependancestarts.add(pdl2_dependancestart);
    }
    public List<pDL2_DependanceFinish> getPdl2_dependancefinishs() {
        return pdl2_dependancefinishs;
    }

    public void addPdl2_dependancefinish(Pdl2_dependancefinish pdl2_dependancefinish) {
        this.pdl2_dependancefinishs.add(pdl2_dependancefinish);
    }
    public pDL2_DependanceStart getPdl2_dependancestart() {
        return pdl2_dependancestart;
    }

    public void setPdl2_dependancestart(pDL2_DependanceStart pdl2_dependancestart) {
        this.pdl2_dependancestart = pdl2_dependancestart;
    }
    public pDL2_DependanceFinish getPdl2_dependancefinish() {
        return pdl2_dependancefinish;
    }

    public void setPdl2_dependancefinish(pDL2_DependanceFinish pdl2_dependancefinish) {
        this.pdl2_dependancefinish = pdl2_dependancefinish;
    }

}