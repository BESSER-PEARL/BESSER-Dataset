





import java.util.List;
import java.util.ArrayList;

public class commons_JavaClassLinked  {

    private String javaClassName;
    private String javaClass;
    private String javaClassStatus;



    public commons_JavaClassLinked(
        String javaClassName,        String javaClass,        String javaClassStatus    ) {
        this.javaClassName = javaClassName;
        this.javaClass = javaClass;
        this.javaClassStatus = javaClassStatus;
    }


    public String getJavaclassname() {
        return javaClassName;
    }

    public void setJavaclassname(String javaClassName) {
        this.javaClassName = javaClassName;
    }
    public String getJavaclass() {
        return javaClass;
    }

    public void setJavaclass(String javaClass) {
        this.javaClass = javaClass;
    }
    public String getJavaclassstatus() {
        return javaClassStatus;
    }

    public void setJavaclassstatus(String javaClassStatus) {
        this.javaClassStatus = javaClassStatus;
    }


}