





import java.util.List;
import java.util.ArrayList;

public class avm_CompoundProperty extends Property {






    private avm_CompoundProperty avm_compoundproperty;




    private List<avm_PrimitiveProperty> avm_primitivepropertys;


    public avm_CompoundProperty(
    ) {
        super(
        );
        this.avm_primitivepropertys = new ArrayList<>();
    }

    public avm_CompoundProperty(
        ArrayList<avm_PrimitiveProperty> avm_primitivepropertys    ) {
        this.avm_primitivepropertys = avm_primitivepropertys;
    }


    public avm_CompoundProperty getAvm_compoundproperty() {
        return avm_compoundproperty;
    }

    public void setAvm_compoundproperty(avm_CompoundProperty avm_compoundproperty) {
        this.avm_compoundproperty = avm_compoundproperty;
    }
    public List<avm_PrimitiveProperty> getAvm_primitivepropertys() {
        return avm_primitivepropertys;
    }

    public void addAvm_primitiveproperty(Avm_primitiveproperty avm_primitiveproperty) {
        this.avm_primitivepropertys.add(avm_primitiveproperty);
    }

}