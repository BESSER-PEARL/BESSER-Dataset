





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Classifier extends Element {

    private boolean isAbstract;



    public UML2WithID_Classifier(
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