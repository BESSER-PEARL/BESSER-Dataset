





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Interface extends Classifier {

    private boolean isActive;
    private String redefinedInterface;





    private List<UMLModel_Operation> umlmodel_operations;


    public UMLModel_Interface(
        boolean isActive,        String redefinedInterface    ) {
        super(
        );
        this.isActive = isActive;
        this.redefinedInterface = redefinedInterface;
        this.umlmodel_operations = new ArrayList<>();
    }

    public UMLModel_Interface(
        boolean isActive,        String redefinedInterface        ArrayList<UMLModel_Operation> umlmodel_operations    ) {
        this.isActive = isActive;
        this.redefinedInterface = redefinedInterface;
        this.umlmodel_operations = umlmodel_operations;
    }

    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }
    public String getRedefinedinterface() {
        return redefinedInterface;
    }

    public void setRedefinedinterface(String redefinedInterface) {
        this.redefinedInterface = redefinedInterface;
    }

    public List<UMLModel_Operation> getUmlmodel_operations() {
        return umlmodel_operations;
    }

    public void addUmlmodel_operation(Umlmodel_operation umlmodel_operation) {
        this.umlmodel_operations.add(umlmodel_operation);
    }

}