





import java.util.List;
import java.util.ArrayList;

public class adb_LoopParameterSpecification  {

    private String identifier;





    private adb_IterationScheme adb_iterationscheme;




    private adb_DiscreteSubtypeDefinition adb_discretesubtypedefinition;


    public adb_LoopParameterSpecification(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public adb_IterationScheme getAdb_iterationscheme() {
        return adb_iterationscheme;
    }

    public void setAdb_iterationscheme(adb_IterationScheme adb_iterationscheme) {
        this.adb_iterationscheme = adb_iterationscheme;
    }
    public adb_DiscreteSubtypeDefinition getAdb_discretesubtypedefinition() {
        return adb_discretesubtypedefinition;
    }

    public void setAdb_discretesubtypedefinition(adb_DiscreteSubtypeDefinition adb_discretesubtypedefinition) {
        this.adb_discretesubtypedefinition = adb_discretesubtypedefinition;
    }

}