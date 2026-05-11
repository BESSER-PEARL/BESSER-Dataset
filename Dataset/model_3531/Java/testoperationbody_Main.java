





import java.util.List;
import java.util.ArrayList;

public class testoperationbody_Main  {

    private boolean singlebool;
    private int listint;





    private List<testoperationbody_Parent> testoperationbody_parents;


    public testoperationbody_Main(
        boolean singlebool,        int listint    ) {
        this.singlebool = singlebool;
        this.listint = listint;
        this.testoperationbody_parents = new ArrayList<>();
    }

    public testoperationbody_Main(
        boolean singlebool,        int listint        ArrayList<testoperationbody_Parent> testoperationbody_parents    ) {
        this.singlebool = singlebool;
        this.listint = listint;
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

    public List<testoperationbody_Parent> getTestoperationbody_parents() {
        return testoperationbody_parents;
    }

    public void addTestoperationbody_parent(Testoperationbody_parent testoperationbody_parent) {
        this.testoperationbody_parents.add(testoperationbody_parent);
    }

}