





import java.util.List;
import java.util.ArrayList;

public class vcml_Function extends ConstraintRestriction, SimpleStatement, FunctionOrTable, Condition {






    private List<vcml_Characteristic> vcml_characteristics;




    private vcml_VariantFunction vcml_variantfunction;




    private List<vcml_Literal> vcml_literals;


    public vcml_Function(
    ) {
        super(
        );
        this.vcml_characteristics = new ArrayList<>();
        this.vcml_literals = new ArrayList<>();
    }

    public vcml_Function(
        ArrayList<vcml_Characteristic> vcml_characteristics,        ArrayList<vcml_Literal> vcml_literals    ) {
        this.vcml_characteristics = vcml_characteristics;
        this.vcml_literals = vcml_literals;
    }


    public List<vcml_Characteristic> getVcml_characteristics() {
        return vcml_characteristics;
    }

    public void addVcml_characteristic(Vcml_characteristic vcml_characteristic) {
        this.vcml_characteristics.add(vcml_characteristic);
    }
    public vcml_VariantFunction getVcml_variantfunction() {
        return vcml_variantfunction;
    }

    public void setVcml_variantfunction(vcml_VariantFunction vcml_variantfunction) {
        this.vcml_variantfunction = vcml_variantfunction;
    }
    public List<vcml_Literal> getVcml_literals() {
        return vcml_literals;
    }

    public void addVcml_literal(Vcml_literal vcml_literal) {
        this.vcml_literals.add(vcml_literal);
    }

}