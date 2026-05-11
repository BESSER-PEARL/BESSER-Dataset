





import java.util.List;
import java.util.ArrayList;

public class sADL_NamedStructureAnnotation  {






    private sADL_SadlResource sadl_sadlresource;




    private List<sADL_SadlExplicitValue> sadl_sadlexplicitvalues;


    public sADL_NamedStructureAnnotation(
    ) {
        this.sadl_sadlexplicitvalues = new ArrayList<>();
    }

    public sADL_NamedStructureAnnotation(
        ArrayList<sADL_SadlExplicitValue> sadl_sadlexplicitvalues    ) {
        this.sadl_sadlexplicitvalues = sadl_sadlexplicitvalues;
    }


    public sADL_SadlResource getSadl_sadlresource() {
        return sadl_sadlresource;
    }

    public void setSadl_sadlresource(sADL_SadlResource sadl_sadlresource) {
        this.sadl_sadlresource = sadl_sadlresource;
    }
    public List<sADL_SadlExplicitValue> getSadl_sadlexplicitvalues() {
        return sadl_sadlexplicitvalues;
    }

    public void addSadl_sadlexplicitvalue(Sadl_sadlexplicitvalue sadl_sadlexplicitvalue) {
        this.sadl_sadlexplicitvalues.add(sadl_sadlexplicitvalue);
    }

}