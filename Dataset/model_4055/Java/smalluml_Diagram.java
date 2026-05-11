





import java.util.List;
import java.util.ArrayList;

public class smalluml_Diagram  {






    private List<smalluml_Association> smalluml_associations;




    private List<smalluml_Class> smalluml_classs;




    private List<smalluml_Heritage> smalluml_heritages;


    public smalluml_Diagram(
    ) {
        this.smalluml_associations = new ArrayList<>();
        this.smalluml_classs = new ArrayList<>();
        this.smalluml_heritages = new ArrayList<>();
    }

    public smalluml_Diagram(
        ArrayList<smalluml_Association> smalluml_associations,        ArrayList<smalluml_Class> smalluml_classs,        ArrayList<smalluml_Heritage> smalluml_heritages    ) {
        this.smalluml_associations = smalluml_associations;
        this.smalluml_classs = smalluml_classs;
        this.smalluml_heritages = smalluml_heritages;
    }


    public List<smalluml_Association> getSmalluml_associations() {
        return smalluml_associations;
    }

    public void addSmalluml_association(Smalluml_association smalluml_association) {
        this.smalluml_associations.add(smalluml_association);
    }
    public List<smalluml_Class> getSmalluml_classs() {
        return smalluml_classs;
    }

    public void addSmalluml_class(Smalluml_class smalluml_class) {
        this.smalluml_classs.add(smalluml_class);
    }
    public List<smalluml_Heritage> getSmalluml_heritages() {
        return smalluml_heritages;
    }

    public void addSmalluml_heritage(Smalluml_heritage smalluml_heritage) {
        this.smalluml_heritages.add(smalluml_heritage);
    }

}