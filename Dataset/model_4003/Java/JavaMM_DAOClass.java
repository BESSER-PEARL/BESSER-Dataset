





import java.util.List;
import java.util.ArrayList;

public class JavaMM_DAOClass extends Class {






    private JavaMM_TestClass javamm_testclass;




    private List<JavaMM_EntityClass> javamm_entityclasss;


    public JavaMM_DAOClass(
    ) {
        super(
        );
        this.javamm_entityclasss = new ArrayList<>();
    }

    public JavaMM_DAOClass(
        ArrayList<JavaMM_EntityClass> javamm_entityclasss    ) {
        this.javamm_entityclasss = javamm_entityclasss;
    }


    public JavaMM_TestClass getJavamm_testclass() {
        return javamm_testclass;
    }

    public void setJavamm_testclass(JavaMM_TestClass javamm_testclass) {
        this.javamm_testclass = javamm_testclass;
    }
    public List<JavaMM_EntityClass> getJavamm_entityclasss() {
        return javamm_entityclasss;
    }

    public void addJavamm_entityclass(Javamm_entityclass javamm_entityclass) {
        this.javamm_entityclasss.add(javamm_entityclass);
    }

}