





import java.util.List;
import java.util.ArrayList;

public class familyleft2_Family  {






    private familyleft2_Father familyleft2_father;




    private familyleft2_Daughter familyleft2_daughter;




    private familyleft2_Mother familyleft2_mother;




    private familyleft2_Son familyleft2_son;




    private List<familyleft2_Daughter> familyleft2_daughters;




    private List<familyleft2_Son> familyleft2_sons;




    private familyleft2_Mother familyleft2_mother;




    private familyleft2_Father familyleft2_father;


    public familyleft2_Family(
    ) {
        this.familyleft2_daughters = new ArrayList<>();
        this.familyleft2_sons = new ArrayList<>();
    }

    public familyleft2_Family(
        ArrayList<familyleft2_Daughter> familyleft2_daughters,        ArrayList<familyleft2_Son> familyleft2_sons    ) {
        this.familyleft2_daughters = familyleft2_daughters;
        this.familyleft2_sons = familyleft2_sons;
    }


    public familyleft2_Father getFamilyleft2_father() {
        return familyleft2_father;
    }

    public void setFamilyleft2_father(familyleft2_Father familyleft2_father) {
        this.familyleft2_father = familyleft2_father;
    }
    public familyleft2_Daughter getFamilyleft2_daughter() {
        return familyleft2_daughter;
    }

    public void setFamilyleft2_daughter(familyleft2_Daughter familyleft2_daughter) {
        this.familyleft2_daughter = familyleft2_daughter;
    }
    public familyleft2_Mother getFamilyleft2_mother() {
        return familyleft2_mother;
    }

    public void setFamilyleft2_mother(familyleft2_Mother familyleft2_mother) {
        this.familyleft2_mother = familyleft2_mother;
    }
    public familyleft2_Son getFamilyleft2_son() {
        return familyleft2_son;
    }

    public void setFamilyleft2_son(familyleft2_Son familyleft2_son) {
        this.familyleft2_son = familyleft2_son;
    }
    public List<familyleft2_Daughter> getFamilyleft2_daughters() {
        return familyleft2_daughters;
    }

    public void addFamilyleft2_daughter(Familyleft2_daughter familyleft2_daughter) {
        this.familyleft2_daughters.add(familyleft2_daughter);
    }
    public List<familyleft2_Son> getFamilyleft2_sons() {
        return familyleft2_sons;
    }

    public void addFamilyleft2_son(Familyleft2_son familyleft2_son) {
        this.familyleft2_sons.add(familyleft2_son);
    }
    public familyleft2_Mother getFamilyleft2_mother() {
        return familyleft2_mother;
    }

    public void setFamilyleft2_mother(familyleft2_Mother familyleft2_mother) {
        this.familyleft2_mother = familyleft2_mother;
    }
    public familyleft2_Father getFamilyleft2_father() {
        return familyleft2_father;
    }

    public void setFamilyleft2_father(familyleft2_Father familyleft2_father) {
        this.familyleft2_father = familyleft2_father;
    }

}