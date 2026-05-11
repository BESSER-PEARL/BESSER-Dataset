





import java.util.List;
import java.util.ArrayList;

public class UML_14_GeneralizableElement extends ModelElement {

    private boolean isAbstract;



    public UML_14_GeneralizableElement(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
    }


    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }


}