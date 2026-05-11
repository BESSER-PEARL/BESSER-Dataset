





import java.util.List;
import java.util.ArrayList;

public class testmodel_TestElementContainer  {






    private List<testmodel_TestElement> testmodel_testelements;




    private testmodel_TestElement testmodel_testelement;


    public testmodel_TestElementContainer(
    ) {
        this.testmodel_testelements = new ArrayList<>();
    }

    public testmodel_TestElementContainer(
        ArrayList<testmodel_TestElement> testmodel_testelements    ) {
        this.testmodel_testelements = testmodel_testelements;
    }


    public List<testmodel_TestElement> getTestmodel_testelements() {
        return testmodel_testelements;
    }

    public void addTestmodel_testelement(Testmodel_testelement testmodel_testelement) {
        this.testmodel_testelements.add(testmodel_testelement);
    }
    public testmodel_TestElement getTestmodel_testelement() {
        return testmodel_testelement;
    }

    public void setTestmodel_testelement(testmodel_TestElement testmodel_testelement) {
        this.testmodel_testelement = testmodel_testelement;
    }

}