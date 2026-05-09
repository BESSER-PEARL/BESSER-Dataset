





import java.util.List;
import java.util.ArrayList;

public class basecs_PathNameCS extends ElementCS, Pivotable {

    private String scopeFilter;





    private basecs_ModelElementRefCS basecs_modelelementrefcs;




    private basecs_ElementCS basecs_elementcs;




    private basecs_ImportCS basecs_importcs;


    public basecs_PathNameCS(
        String scopeFilter    ) {
        super(
        );
        this.scopeFilter = scopeFilter;
    }


    public String getScopefilter() {
        return scopeFilter;
    }

    public void setScopefilter(String scopeFilter) {
        this.scopeFilter = scopeFilter;
    }

    public basecs_ModelElementRefCS getBasecs_modelelementrefcs() {
        return basecs_modelelementrefcs;
    }

    public void setBasecs_modelelementrefcs(basecs_ModelElementRefCS basecs_modelelementrefcs) {
        this.basecs_modelelementrefcs = basecs_modelelementrefcs;
    }
    public basecs_ElementCS getBasecs_elementcs() {
        return basecs_elementcs;
    }

    public void setBasecs_elementcs(basecs_ElementCS basecs_elementcs) {
        this.basecs_elementcs = basecs_elementcs;
    }
    public basecs_ImportCS getBasecs_importcs() {
        return basecs_importcs;
    }

    public void setBasecs_importcs(basecs_ImportCS basecs_importcs) {
        this.basecs_importcs = basecs_importcs;
    }

}