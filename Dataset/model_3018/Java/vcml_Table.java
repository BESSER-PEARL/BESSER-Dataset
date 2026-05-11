





import java.util.List;
import java.util.ArrayList;

public class vcml_Table extends ConstraintRestriction, SimpleStatement, FunctionOrTable, Condition {






    private List<vcml_Characteristic> vcml_characteristics;




    private List<vcml_Literal> vcml_literals;




    private vcml_VariantTable vcml_varianttable;


    public vcml_Table(
    ) {
        super(
        );
        this.vcml_characteristics = new ArrayList<>();
        this.vcml_literals = new ArrayList<>();
    }

    public vcml_Table(
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
    public List<vcml_Literal> getVcml_literals() {
        return vcml_literals;
    }

    public void addVcml_literal(Vcml_literal vcml_literal) {
        this.vcml_literals.add(vcml_literal);
    }
    public vcml_VariantTable getVcml_varianttable() {
        return vcml_varianttable;
    }

    public void setVcml_varianttable(vcml_VariantTable vcml_varianttable) {
        this.vcml_varianttable = vcml_varianttable;
    }

}