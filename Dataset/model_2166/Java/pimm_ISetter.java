





import java.util.List;
import java.util.ArrayList;

public class pimm_ISetter  {






    private pimm_Dependency pimm_dependency;




    private List<pimm_Dependency> pimm_dependencys;


    public pimm_ISetter(
    ) {
        this.pimm_dependencys = new ArrayList<>();
    }

    public pimm_ISetter(
        ArrayList<pimm_Dependency> pimm_dependencys    ) {
        this.pimm_dependencys = pimm_dependencys;
    }


    public pimm_Dependency getPimm_dependency() {
        return pimm_dependency;
    }

    public void setPimm_dependency(pimm_Dependency pimm_dependency) {
        this.pimm_dependency = pimm_dependency;
    }
    public List<pimm_Dependency> getPimm_dependencys() {
        return pimm_dependencys;
    }

    public void addPimm_dependency(Pimm_dependency pimm_dependency) {
        this.pimm_dependencys.add(pimm_dependency);
    }

}