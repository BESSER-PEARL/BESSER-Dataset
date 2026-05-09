





import java.util.List;
import java.util.ArrayList;

public class emof_Class extends Type {

    private String isAbstract;





    private emof_Class emof_class;


    public emof_Class(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
    }


    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public emof_Class getEmof_class() {
        return emof_class;
    }

    public void setEmof_class(emof_Class emof_class) {
        this.emof_class = emof_class;
    }

}