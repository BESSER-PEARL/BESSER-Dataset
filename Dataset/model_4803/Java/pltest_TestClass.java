





import java.util.List;
import java.util.ArrayList;

public class pltest_TestClass extends TestClassifier {






    private List<pltest_TestClassifier> pltest_testclassifiers;


    public pltest_TestClass(
    ) {
        super(
        );
        this.pltest_testclassifiers = new ArrayList<>();
    }

    public pltest_TestClass(
        ArrayList<pltest_TestClassifier> pltest_testclassifiers    ) {
        this.pltest_testclassifiers = pltest_testclassifiers;
    }


    public List<pltest_TestClassifier> getPltest_testclassifiers() {
        return pltest_testclassifiers;
    }

    public void addPltest_testclassifier(Pltest_testclassifier pltest_testclassifier) {
        this.pltest_testclassifiers.add(pltest_testclassifier);
    }

}