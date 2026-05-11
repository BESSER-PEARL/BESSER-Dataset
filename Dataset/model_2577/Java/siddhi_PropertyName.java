





import java.util.List;
import java.util.ArrayList;

public class siddhi_PropertyName  {






    private siddhi_AnnotationElement siddhi_annotationelement;




    private List<siddhi_Name> siddhi_names;


    public siddhi_PropertyName(
    ) {
        this.siddhi_names = new ArrayList<>();
    }

    public siddhi_PropertyName(
        ArrayList<siddhi_Name> siddhi_names    ) {
        this.siddhi_names = siddhi_names;
    }


    public siddhi_AnnotationElement getSiddhi_annotationelement() {
        return siddhi_annotationelement;
    }

    public void setSiddhi_annotationelement(siddhi_AnnotationElement siddhi_annotationelement) {
        this.siddhi_annotationelement = siddhi_annotationelement;
    }
    public List<siddhi_Name> getSiddhi_names() {
        return siddhi_names;
    }

    public void addSiddhi_name(Siddhi_name siddhi_name) {
        this.siddhi_names.add(siddhi_name);
    }

}