





import java.util.List;
import java.util.ArrayList;

public class testLanguage_Greeting  {

    private String name;





    private testLanguage_Model testlanguage_model;


    public testLanguage_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public testLanguage_Model getTestlanguage_model() {
        return testlanguage_model;
    }

    public void setTestlanguage_model(testLanguage_Model testlanguage_model) {
        this.testlanguage_model = testlanguage_model;
    }

}