





import java.util.List;
import java.util.ArrayList;

public class ecore_EPackage  {






    private List<ecore_EClass> ecore_eclasss;




    private ecore_EClass ecore_eclass;


    public ecore_EPackage(
    ) {
        this.ecore_eclasss = new ArrayList<>();
    }

    public ecore_EPackage(
        ArrayList<ecore_EClass> ecore_eclasss    ) {
        this.ecore_eclasss = ecore_eclasss;
    }


    public List<ecore_EClass> getEcore_eclasss() {
        return ecore_eclasss;
    }

    public void addEcore_eclass(Ecore_eclass ecore_eclass) {
        this.ecore_eclasss.add(ecore_eclass);
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }

}