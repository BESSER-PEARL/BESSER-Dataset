





import java.util.List;
import java.util.ArrayList;

public class avm_ParametricEnumeratedValue extends ValueExpressionType {






    private avm_FixedValue avm_fixedvalue;




    private List<avm_ValueExpressionType> avm_valueexpressiontypes;


    public avm_ParametricEnumeratedValue(
    ) {
        super(
        );
        this.avm_valueexpressiontypes = new ArrayList<>();
    }

    public avm_ParametricEnumeratedValue(
        ArrayList<avm_ValueExpressionType> avm_valueexpressiontypes    ) {
        this.avm_valueexpressiontypes = avm_valueexpressiontypes;
    }


    public avm_FixedValue getAvm_fixedvalue() {
        return avm_fixedvalue;
    }

    public void setAvm_fixedvalue(avm_FixedValue avm_fixedvalue) {
        this.avm_fixedvalue = avm_fixedvalue;
    }
    public List<avm_ValueExpressionType> getAvm_valueexpressiontypes() {
        return avm_valueexpressiontypes;
    }

    public void addAvm_valueexpressiontype(Avm_valueexpressiontype avm_valueexpressiontype) {
        this.avm_valueexpressiontypes.add(avm_valueexpressiontype);
    }

}