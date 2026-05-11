





import java.util.List;
import java.util.ArrayList;

public class dcmddandroid_AbstractClass extends ModelElement, EVisibility {

    private boolean isAbstract;



    public dcmddandroid_AbstractClass(
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