





import java.util.List;
import java.util.ArrayList;

public class UML2_Classifier extends Namespace, RedefinableElement, Type {

    private boolean isAbstract;



    public UML2_Classifier(
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