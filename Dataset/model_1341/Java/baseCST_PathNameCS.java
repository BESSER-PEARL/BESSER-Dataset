





import java.util.List;
import java.util.ArrayList;

public class baseCST_PathNameCS extends Pivotable, ElementCS {

    private String scopeFilter;





    private baseCST_Element basecst_element;




    private baseCST_ModelElementRefCS basecst_modelelementrefcs;




    private baseCST_ElementCS basecst_elementcs;




    private baseCST_ImportCS basecst_importcs;




    private baseCST_TypedTypeRefCS basecst_typedtyperefcs;


    public baseCST_PathNameCS(
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

    public baseCST_Element getBasecst_element() {
        return basecst_element;
    }

    public void setBasecst_element(baseCST_Element basecst_element) {
        this.basecst_element = basecst_element;
    }
    public baseCST_ModelElementRefCS getBasecst_modelelementrefcs() {
        return basecst_modelelementrefcs;
    }

    public void setBasecst_modelelementrefcs(baseCST_ModelElementRefCS basecst_modelelementrefcs) {
        this.basecst_modelelementrefcs = basecst_modelelementrefcs;
    }
    public baseCST_ElementCS getBasecst_elementcs() {
        return basecst_elementcs;
    }

    public void setBasecst_elementcs(baseCST_ElementCS basecst_elementcs) {
        this.basecst_elementcs = basecst_elementcs;
    }
    public baseCST_ImportCS getBasecst_importcs() {
        return basecst_importcs;
    }

    public void setBasecst_importcs(baseCST_ImportCS basecst_importcs) {
        this.basecst_importcs = basecst_importcs;
    }
    public baseCST_TypedTypeRefCS getBasecst_typedtyperefcs() {
        return basecst_typedtyperefcs;
    }

    public void setBasecst_typedtyperefcs(baseCST_TypedTypeRefCS basecst_typedtyperefcs) {
        this.basecst_typedtyperefcs = basecst_typedtyperefcs;
    }

}