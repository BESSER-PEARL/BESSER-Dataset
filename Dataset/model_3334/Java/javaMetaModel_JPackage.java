





import java.util.List;
import java.util.ArrayList;

public class javaMetaModel_JPackage extends JElement {






    private List<javaMetaModel_JClass> javametamodel_jclasss;




    private javaMetaModel_JClass javametamodel_jclass;


    public javaMetaModel_JPackage(
    ) {
        super(
        );
        this.javametamodel_jclasss = new ArrayList<>();
    }

    public javaMetaModel_JPackage(
        ArrayList<javaMetaModel_JClass> javametamodel_jclasss    ) {
        this.javametamodel_jclasss = javametamodel_jclasss;
    }


    public List<javaMetaModel_JClass> getJavametamodel_jclasss() {
        return javametamodel_jclasss;
    }

    public void addJavametamodel_jclass(Javametamodel_jclass javametamodel_jclass) {
        this.javametamodel_jclasss.add(javametamodel_jclass);
    }
    public javaMetaModel_JClass getJavametamodel_jclass() {
        return javametamodel_jclass;
    }

    public void setJavametamodel_jclass(javaMetaModel_JClass javametamodel_jclass) {
        this.javametamodel_jclass = javametamodel_jclass;
    }

}