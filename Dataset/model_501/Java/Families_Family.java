





import java.util.List;
import java.util.ArrayList;

public class Families_Family  {

    private String lastName;





    private Families_Father families_father;




    private Families_Mother families_mother;




    private Families_Daughter families_daughter;




    private List<Families_Son> families_sons;




    private Families_Mother families_mother;




    private Families_Son families_son;




    private List<Families_Daughter> families_daughters;




    private Families_Father families_father;


    public Families_Family(
        String lastName    ) {
        this.lastName = lastName;
        this.families_sons = new ArrayList<>();
        this.families_daughters = new ArrayList<>();
    }

    public Families_Family(
        String lastName        ArrayList<Families_Son> families_sons,        ArrayList<Families_Daughter> families_daughters    ) {
        this.lastName = lastName;
        this.families_sons = families_sons;
        this.families_daughters = families_daughters;
    }

    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }

    public Families_Father getFamilies_father() {
        return families_father;
    }

    public void setFamilies_father(Families_Father families_father) {
        this.families_father = families_father;
    }
    public Families_Mother getFamilies_mother() {
        return families_mother;
    }

    public void setFamilies_mother(Families_Mother families_mother) {
        this.families_mother = families_mother;
    }
    public Families_Daughter getFamilies_daughter() {
        return families_daughter;
    }

    public void setFamilies_daughter(Families_Daughter families_daughter) {
        this.families_daughter = families_daughter;
    }
    public List<Families_Son> getFamilies_sons() {
        return families_sons;
    }

    public void addFamilies_son(Families_son families_son) {
        this.families_sons.add(families_son);
    }
    public Families_Mother getFamilies_mother() {
        return families_mother;
    }

    public void setFamilies_mother(Families_Mother families_mother) {
        this.families_mother = families_mother;
    }
    public Families_Son getFamilies_son() {
        return families_son;
    }

    public void setFamilies_son(Families_Son families_son) {
        this.families_son = families_son;
    }
    public List<Families_Daughter> getFamilies_daughters() {
        return families_daughters;
    }

    public void addFamilies_daughter(Families_daughter families_daughter) {
        this.families_daughters.add(families_daughter);
    }
    public Families_Father getFamilies_father() {
        return families_father;
    }

    public void setFamilies_father(Families_Father families_father) {
        this.families_father = families_father;
    }

}