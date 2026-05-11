





import java.util.List;
import java.util.ArrayList;

public class Classes_Kernel_Classifier extends Kernel_Namespace, Kernel_RedefinableElement, Kernel_Type {

    private boolean isFinalSpecialization;
    private boolean isAbstract;





    private List<NamedElement> namedelements;


    public Classes_Kernel_Classifier(
        boolean isFinalSpecialization,        boolean isAbstract    ) {
        super(
        );
        this.isFinalSpecialization = isFinalSpecialization;
        this.isAbstract = isAbstract;
        this.namedelements = new ArrayList<>();
    }

    public Classes_Kernel_Classifier(
        boolean isFinalSpecialization,        boolean isAbstract        ArrayList<NamedElement> namedelements    ) {
        this.isFinalSpecialization = isFinalSpecialization;
        this.isAbstract = isAbstract;
        this.namedelements = namedelements;
    }

    public boolean getIsfinalspecialization() {
        return isFinalSpecialization;
    }

    public void setIsfinalspecialization(boolean isFinalSpecialization) {
        this.isFinalSpecialization = isFinalSpecialization;
    }
    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<NamedElement> getNamedelements() {
        return namedelements;
    }

    public void addNamedelement(Namedelement namedelement) {
        this.namedelements.add(namedelement);
    }

}