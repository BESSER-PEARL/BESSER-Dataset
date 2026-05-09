





import java.util.List;
import java.util.ArrayList;

public class org_structure_Class extends ParameterizedType {

    private String isAbstract;
    private String name;



    public org_structure_Class(
        String isAbstract,        String name    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.name = name;
    }


    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}