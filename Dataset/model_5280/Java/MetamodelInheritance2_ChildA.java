





import java.util.List;
import java.util.ArrayList;

public class MetamodelInheritance2_ChildA extends BaseContaineeA {






    private List<MetamodelInheritance2_BaseContaineeC> metamodelinheritance2_basecontaineecs;




    private List<MetamodelInheritance2_ChildB> metamodelinheritance2_childbs;




    private MetamodelInheritance2_ChildB metamodelinheritance2_childb;


    public MetamodelInheritance2_ChildA(
    ) {
        super(
        );
        this.metamodelinheritance2_basecontaineecs = new ArrayList<>();
        this.metamodelinheritance2_childbs = new ArrayList<>();
    }

    public MetamodelInheritance2_ChildA(
        ArrayList<MetamodelInheritance2_BaseContaineeC> metamodelinheritance2_basecontaineecs,        ArrayList<MetamodelInheritance2_ChildB> metamodelinheritance2_childbs    ) {
        this.metamodelinheritance2_basecontaineecs = metamodelinheritance2_basecontaineecs;
        this.metamodelinheritance2_childbs = metamodelinheritance2_childbs;
    }


    public List<MetamodelInheritance2_BaseContaineeC> getMetamodelinheritance2_basecontaineecs() {
        return metamodelinheritance2_basecontaineecs;
    }

    public void addMetamodelinheritance2_basecontaineec(Metamodelinheritance2_basecontaineec metamodelinheritance2_basecontaineec) {
        this.metamodelinheritance2_basecontaineecs.add(metamodelinheritance2_basecontaineec);
    }
    public List<MetamodelInheritance2_ChildB> getMetamodelinheritance2_childbs() {
        return metamodelinheritance2_childbs;
    }

    public void addMetamodelinheritance2_childb(Metamodelinheritance2_childb metamodelinheritance2_childb) {
        this.metamodelinheritance2_childbs.add(metamodelinheritance2_childb);
    }
    public MetamodelInheritance2_ChildB getMetamodelinheritance2_childb() {
        return metamodelinheritance2_childb;
    }

    public void setMetamodelinheritance2_childb(MetamodelInheritance2_ChildB metamodelinheritance2_childb) {
        this.metamodelinheritance2_childb = metamodelinheritance2_childb;
    }

}