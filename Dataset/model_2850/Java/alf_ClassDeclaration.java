





import java.util.List;
import java.util.ArrayList;

public class alf_ClassDeclaration  {

    private boolean isAbstract;





    private alf_ClassifierSignature alf_classifiersignature;


    public alf_ClassDeclaration(
        boolean isAbstract    ) {
        this.isAbstract = isAbstract;
    }


    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public alf_ClassifierSignature getAlf_classifiersignature() {
        return alf_classifiersignature;
    }

    public void setAlf_classifiersignature(alf_ClassifierSignature alf_classifiersignature) {
        this.alf_classifiersignature = alf_classifiersignature;
    }

}