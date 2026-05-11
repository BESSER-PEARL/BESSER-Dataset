





import java.util.List;
import java.util.ArrayList;

public class testPackage_TestElementB extends TestElementA {






    private List<testPackage_TestElementA> testpackage_testelementas;


    public testPackage_TestElementB(
    ) {
        super(
        );
        this.testpackage_testelementas = new ArrayList<>();
    }

    public testPackage_TestElementB(
        ArrayList<testPackage_TestElementA> testpackage_testelementas    ) {
        this.testpackage_testelementas = testpackage_testelementas;
    }


    public List<testPackage_TestElementA> getTestpackage_testelementas() {
        return testpackage_testelementas;
    }

    public void addTestpackage_testelementa(Testpackage_testelementa testpackage_testelementa) {
        this.testpackage_testelementas.add(testpackage_testelementa);
    }

}