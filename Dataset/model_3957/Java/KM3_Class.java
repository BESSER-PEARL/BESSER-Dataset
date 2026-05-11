





import java.util.List;
import java.util.ArrayList;

public class KM3_Class extends Classifier {

    private boolean isAbstract;





    private KM3_Class km3_class;


    public KM3_Class(
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

    public KM3_Class getKm3_class() {
        return km3_class;
    }

    public void setKm3_class(KM3_Class km3_class) {
        this.km3_class = km3_class;
    }

}