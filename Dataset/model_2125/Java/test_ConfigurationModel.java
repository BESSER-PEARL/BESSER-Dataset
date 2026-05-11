





import java.util.List;
import java.util.ArrayList;

public class test_ConfigurationModel  {






    private List<test_TestModel> test_testmodels;




    private test_TestModel test_testmodel;


    public test_ConfigurationModel(
    ) {
        this.test_testmodels = new ArrayList<>();
    }

    public test_ConfigurationModel(
        ArrayList<test_TestModel> test_testmodels    ) {
        this.test_testmodels = test_testmodels;
    }


    public List<test_TestModel> getTest_testmodels() {
        return test_testmodels;
    }

    public void addTest_testmodel(Test_testmodel test_testmodel) {
        this.test_testmodels.add(test_testmodel);
    }
    public test_TestModel getTest_testmodel() {
        return test_testmodel;
    }

    public void setTest_testmodel(test_TestModel test_testmodel) {
        this.test_testmodel = test_testmodel;
    }

}