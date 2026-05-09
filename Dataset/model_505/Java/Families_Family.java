





import java.util.List;
import java.util.ArrayList;

public class Families_Family  {

    private String lastName;





    private Families_Neighborhood families_neighborhood;




    private List<Families_Child> families_childs;




    private List<Families_Parent> families_parents;




    private List<Families_Parent> families_parents;




    private Families_Country families_country;




    private List<Families_Child> families_childs;




    private Families_Neighborhood families_neighborhood;


    public Families_Family(
        String lastName    ) {
        this.lastName = lastName;
        this.families_childs = new ArrayList<>();
        this.families_parents = new ArrayList<>();
        this.families_parents = new ArrayList<>();
        this.families_childs = new ArrayList<>();
    }

    public Families_Family(
        String lastName        ArrayList<Families_Child> families_childs,        ArrayList<Families_Parent> families_parents,        ArrayList<Families_Parent> families_parents,        ArrayList<Families_Child> families_childs    ) {
        this.lastName = lastName;
        this.families_childs = families_childs;
        this.families_parents = families_parents;
        this.families_parents = families_parents;
        this.families_childs = families_childs;
    }

    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }

    public Families_Neighborhood getFamilies_neighborhood() {
        return families_neighborhood;
    }

    public void setFamilies_neighborhood(Families_Neighborhood families_neighborhood) {
        this.families_neighborhood = families_neighborhood;
    }
    public List<Families_Child> getFamilies_childs() {
        return families_childs;
    }

    public void addFamilies_child(Families_child families_child) {
        this.families_childs.add(families_child);
    }
    public List<Families_Parent> getFamilies_parents() {
        return families_parents;
    }

    public void addFamilies_parent(Families_parent families_parent) {
        this.families_parents.add(families_parent);
    }
    public List<Families_Parent> getFamilies_parents() {
        return families_parents;
    }

    public void addFamilies_parent(Families_parent families_parent) {
        this.families_parents.add(families_parent);
    }
    public Families_Country getFamilies_country() {
        return families_country;
    }

    public void setFamilies_country(Families_Country families_country) {
        this.families_country = families_country;
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

}