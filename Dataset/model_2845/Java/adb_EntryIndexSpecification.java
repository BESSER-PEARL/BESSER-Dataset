





import java.util.List;
import java.util.ArrayList;

public class adb_EntryIndexSpecification  {

    private String name;





    private adb_EntryBodyFormalPart adb_entrybodyformalpart;




    private adb_DiscreteSubtypeDefinition adb_discretesubtypedefinition;


    public adb_EntryIndexSpecification(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adb_EntryBodyFormalPart getAdb_entrybodyformalpart() {
        return adb_entrybodyformalpart;
    }

    public void setAdb_entrybodyformalpart(adb_EntryBodyFormalPart adb_entrybodyformalpart) {
        this.adb_entrybodyformalpart = adb_entrybodyformalpart;
    }
    public adb_DiscreteSubtypeDefinition getAdb_discretesubtypedefinition() {
        return adb_discretesubtypedefinition;
    }

    public void setAdb_discretesubtypedefinition(adb_DiscreteSubtypeDefinition adb_discretesubtypedefinition) {
        this.adb_discretesubtypedefinition = adb_discretesubtypedefinition;
    }

}