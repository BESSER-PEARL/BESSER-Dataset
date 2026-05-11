





import java.util.List;
import java.util.ArrayList;

public class testoperationbody_Main  {

    private boolean singlebool;
    private int listint;





    private List<testoperationbody_ConceptA> testoperationbody_conceptas;




    private testoperationbody_ConceptA testoperationbody_concepta;




    private List<testoperationbody_Parent> testoperationbody_parents;


    public testoperationbody_Main(
        boolean singlebool,        int listint    ) {
        this.singlebool = singlebool;
        this.listint = listint;
        this.testoperationbody_conceptas = new ArrayList<>();
        this.testoperationbody_parents = new ArrayList<>();
    }

    public testoperationbody_Main(
        boolean singlebool,        int listint        ArrayList<testoperationbody_ConceptA> testoperationbody_conceptas,        ArrayList<testoperationbody_Parent> testoperationbody_parents    ) {
        this.singlebool = singlebool;
        this.listint = listint;
        this.testoperationbody_conceptas = testoperationbody_conceptas;
        this.testoperationbody_parents = testoperationbody_parents;
    }

    public boolean getSinglebool() {
        return singlebool;
    }

    public void setSinglebool(boolean singlebool) {
        this.singlebool = singlebool;
    }
    public int getListint() {
        return listint;
    }

    public void setListint(int listint) {
        this.listint = listint;
    }

    public List<testoperationbody_ConceptA> getTestoperationbody_conceptas() {
        return testoperationbody_conceptas;
    }

    public void addTestoperationbody_concepta(Testoperationbody_concepta testoperationbody_concepta) {
        this.testoperationbody_conceptas.add(testoperationbody_concepta);
    }
    public testoperationbody_ConceptA getTestoperationbody_concepta() {
        return testoperationbody_concepta;
    }

    public void setTestoperationbody_concepta(testoperationbody_ConceptA testoperationbody_concepta) {
        this.testoperationbody_concepta = testoperationbody_concepta;
    }
    public List<testoperationbody_Parent> getTestoperationbody_parents() {
        return testoperationbody_parents;
    }

    public void addTestoperationbody_parent(Testoperationbody_parent testoperationbody_parent) {
        this.testoperationbody_parents.add(testoperationbody_parent);
    }

}