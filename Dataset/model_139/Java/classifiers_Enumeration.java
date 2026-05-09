





import java.util.List;
import java.util.ArrayList;

public class classifiers_Enumeration extends ConcreteClassifier, Implementor {






    private List<EnumConstant> enumconstants;


    public classifiers_Enumeration(
    ) {
        super(
        );
        this.enumconstants = new ArrayList<>();
    }

    public classifiers_Enumeration(
        ArrayList<EnumConstant> enumconstants    ) {
        this.enumconstants = enumconstants;
    }


    public List<EnumConstant> getEnumconstants() {
        return enumconstants;
    }

    public void addEnumconstant(Enumconstant enumconstant) {
        this.enumconstants.add(enumconstant);
    }

}