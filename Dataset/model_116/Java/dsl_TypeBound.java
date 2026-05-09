





import java.util.List;
import java.util.ArrayList;

public class dsl_TypeBound  {






    private dsl_TypeParameter dsl_typeparameter;




    private List<dsl_ClassOrInterfaceType> dsl_classorinterfacetypes;


    public dsl_TypeBound(
    ) {
        this.dsl_classorinterfacetypes = new ArrayList<>();
    }

    public dsl_TypeBound(
        ArrayList<dsl_ClassOrInterfaceType> dsl_classorinterfacetypes    ) {
        this.dsl_classorinterfacetypes = dsl_classorinterfacetypes;
    }


    public dsl_TypeParameter getDsl_typeparameter() {
        return dsl_typeparameter;
    }

    public void setDsl_typeparameter(dsl_TypeParameter dsl_typeparameter) {
        this.dsl_typeparameter = dsl_typeparameter;
    }
    public List<dsl_ClassOrInterfaceType> getDsl_classorinterfacetypes() {
        return dsl_classorinterfacetypes;
    }

    public void addDsl_classorinterfacetype(Dsl_classorinterfacetype dsl_classorinterfacetype) {
        this.dsl_classorinterfacetypes.add(dsl_classorinterfacetype);
    }

}