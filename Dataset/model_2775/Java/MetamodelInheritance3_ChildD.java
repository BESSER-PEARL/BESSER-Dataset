





import java.util.List;
import java.util.ArrayList;

public class MetamodelInheritance3_ChildD extends ChildContaineeD {






    private List<MetamodelInheritance3_ChildC> metamodelinheritance3_childcs;




    private MetamodelInheritance3_ChildC metamodelinheritance3_childc;


    public MetamodelInheritance3_ChildD(
    ) {
        super(
        );
        this.metamodelinheritance3_childcs = new ArrayList<>();
    }

    public MetamodelInheritance3_ChildD(
        ArrayList<MetamodelInheritance3_ChildC> metamodelinheritance3_childcs    ) {
        this.metamodelinheritance3_childcs = metamodelinheritance3_childcs;
    }


    public List<MetamodelInheritance3_ChildC> getMetamodelinheritance3_childcs() {
        return metamodelinheritance3_childcs;
    }

    public void addMetamodelinheritance3_childc(Metamodelinheritance3_childc metamodelinheritance3_childc) {
        this.metamodelinheritance3_childcs.add(metamodelinheritance3_childc);
    }
    public MetamodelInheritance3_ChildC getMetamodelinheritance3_childc() {
        return metamodelinheritance3_childc;
    }

    public void setMetamodelinheritance3_childc(MetamodelInheritance3_ChildC metamodelinheritance3_childc) {
        this.metamodelinheritance3_childc = metamodelinheritance3_childc;
    }

}