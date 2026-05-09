





import java.util.List;
import java.util.ArrayList;

public class familyright_Family  {






    private List<familyright_Daughter> familyright_daughters;




    private familyright_Father familyright_father;




    private familyright_Father familyright_father;




    private familyright_Daughter familyright_daughter;




    private List<familyright_Son> familyright_sons;




    private familyright_Son familyright_son;


    public familyright_Family(
    ) {
        this.familyright_daughters = new ArrayList<>();
        this.familyright_sons = new ArrayList<>();
    }

    public familyright_Family(
        ArrayList<familyright_Daughter> familyright_daughters,        ArrayList<familyright_Son> familyright_sons    ) {
        this.familyright_daughters = familyright_daughters;
        this.familyright_sons = familyright_sons;
    }


    public List<familyright_Daughter> getFamilyright_daughters() {
        return familyright_daughters;
    }

    public void addFamilyright_daughter(Familyright_daughter familyright_daughter) {
        this.familyright_daughters.add(familyright_daughter);
    }
    public familyright_Father getFamilyright_father() {
        return familyright_father;
    }

    public void setFamilyright_father(familyright_Father familyright_father) {
        this.familyright_father = familyright_father;
    }
    public familyright_Father getFamilyright_father() {
        return familyright_father;
    }

    public void setFamilyright_father(familyright_Father familyright_father) {
        this.familyright_father = familyright_father;
    }
    public familyright_Daughter getFamilyright_daughter() {
        return familyright_daughter;
    }

    public void setFamilyright_daughter(familyright_Daughter familyright_daughter) {
        this.familyright_daughter = familyright_daughter;
    }
    public List<familyright_Son> getFamilyright_sons() {
        return familyright_sons;
    }

    public void addFamilyright_son(Familyright_son familyright_son) {
        this.familyright_sons.add(familyright_son);
    }
    public familyright_Son getFamilyright_son() {
        return familyright_son;
    }

    public void setFamilyright_son(familyright_Son familyright_son) {
        this.familyright_son = familyright_son;
    }

}