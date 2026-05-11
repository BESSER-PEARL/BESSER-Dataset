





import java.util.List;
import java.util.ArrayList;

public class ram_OperationMapping extends Mapping {






    private ram_Operation ram_operation;




    private ram_ClassifierMapping ram_classifiermapping;




    private ram_Operation ram_operation;




    private List<ram_ParameterMapping> ram_parametermappings;


    public ram_OperationMapping(
    ) {
        super(
        );
        this.ram_parametermappings = new ArrayList<>();
    }

    public ram_OperationMapping(
        ArrayList<ram_ParameterMapping> ram_parametermappings    ) {
        this.ram_parametermappings = ram_parametermappings;
    }


    public ram_Operation getRam_operation() {
        return ram_operation;
    }

    public void setRam_operation(ram_Operation ram_operation) {
        this.ram_operation = ram_operation;
    }
    public ram_ClassifierMapping getRam_classifiermapping() {
        return ram_classifiermapping;
    }

    public void setRam_classifiermapping(ram_ClassifierMapping ram_classifiermapping) {
        this.ram_classifiermapping = ram_classifiermapping;
    }
    public ram_Operation getRam_operation() {
        return ram_operation;
    }

    public void setRam_operation(ram_Operation ram_operation) {
        this.ram_operation = ram_operation;
    }
    public List<ram_ParameterMapping> getRam_parametermappings() {
        return ram_parametermappings;
    }

    public void addRam_parametermapping(Ram_parametermapping ram_parametermapping) {
        this.ram_parametermappings.add(ram_parametermapping);
    }

}