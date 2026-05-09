





import java.util.List;
import java.util.ArrayList;

public class Families_School extends NamedElement {






    private List<Families_Child> families_childs;




    private Families_Neighborhood families_neighborhood;




    private Families_Child families_child;


    public Families_School(
    ) {
        super(
        );
        this.families_childs = new ArrayList<>();
    }

    public Families_School(
        ArrayList<Families_Child> families_childs    ) {
        this.families_childs = families_childs;
    }


    public List<Families_Child> getFamilies_childs() {
        return families_childs;
    }

    public void addFamilies_child(Families_child families_child) {
        this.families_childs.add(families_child);
    }
    public Families_Neighborhood getFamilies_neighborhood() {
        return families_neighborhood;
    }

    public void setFamilies_neighborhood(Families_Neighborhood families_neighborhood) {
        this.families_neighborhood = families_neighborhood;
    }
    public Families_Child getFamilies_child() {
        return families_child;
    }

    public void setFamilies_child(Families_Child families_child) {
        this.families_child = families_child;
    }

}