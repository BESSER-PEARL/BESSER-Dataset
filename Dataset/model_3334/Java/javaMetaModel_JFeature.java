





import java.util.List;
import java.util.ArrayList;

public class javaMetaModel_JFeature extends JElement {

    private String visibility;
    private boolean isStatic;





    private javaMetaModel_JClass javametamodel_jclass;




    private javaMetaModel_JClass javametamodel_jclass;


    public javaMetaModel_JFeature(
        String visibility,        boolean isStatic    ) {
        super(
        );
        this.visibility = visibility;
        this.isStatic = isStatic;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }

    public javaMetaModel_JClass getJavametamodel_jclass() {
        return javametamodel_jclass;
    }

    public void setJavametamodel_jclass(javaMetaModel_JClass javametamodel_jclass) {
        this.javametamodel_jclass = javametamodel_jclass;
    }
    public javaMetaModel_JClass getJavametamodel_jclass() {
        return javametamodel_jclass;
    }

    public void setJavametamodel_jclass(javaMetaModel_JClass javametamodel_jclass) {
        this.javametamodel_jclass = javametamodel_jclass;
    }

}