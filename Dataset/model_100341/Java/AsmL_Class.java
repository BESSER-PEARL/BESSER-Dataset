





import java.util.List;
import java.util.ArrayList;

public class AsmL_Class extends AsmLElement {

    private String name;
    private String superClassName;
    private String isAbstract;



    public AsmL_Class(
        String name,        String superClassName,        String isAbstract    ) {
        super(
        );
        this.name = name;
        this.superClassName = superClassName;
        this.isAbstract = isAbstract;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSuperclassname() {
        return superClassName;
    }

    public void setSuperclassname(String superClassName) {
        this.superClassName = superClassName;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }


}