





import java.util.List;
import java.util.ArrayList;

public class javaless_EClassifier extends ENamedElement {

    private String instanceClassName;
    private String instanceClass;
    private String defaultValue;





    private javaless_EPackage javaless_epackage;




    private javaless_EOperation javaless_eoperation;




    private javaless_EPackage javaless_epackage;


    public javaless_EClassifier(
        String instanceClassName,        String instanceClass,        String defaultValue    ) {
        super(
        );
        this.instanceClassName = instanceClassName;
        this.instanceClass = instanceClass;
        this.defaultValue = defaultValue;
    }


    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }
    public String getInstanceclass() {
        return instanceClass;
    }

    public void setInstanceclass(String instanceClass) {
        this.instanceClass = instanceClass;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }

    public javaless_EPackage getJavaless_epackage() {
        return javaless_epackage;
    }

    public void setJavaless_epackage(javaless_EPackage javaless_epackage) {
        this.javaless_epackage = javaless_epackage;
    }
    public javaless_EOperation getJavaless_eoperation() {
        return javaless_eoperation;
    }

    public void setJavaless_eoperation(javaless_EOperation javaless_eoperation) {
        this.javaless_eoperation = javaless_eoperation;
    }
    public javaless_EPackage getJavaless_epackage() {
        return javaless_epackage;
    }

    public void setJavaless_epackage(javaless_EPackage javaless_epackage) {
        this.javaless_epackage = javaless_epackage;
    }

}