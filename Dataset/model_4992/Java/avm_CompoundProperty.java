





import java.util.List;
import java.util.ArrayList;

public class avm_CompoundProperty extends Property {






    private List<avm_PrimitiveProperty> avm_primitivepropertys;




    private List<avm_CompoundProperty> avm_compoundpropertys;


    public avm_CompoundProperty(
    ) {
        super(
        );
        this.avm_primitivepropertys = new ArrayList<>();
        this.avm_compoundpropertys = new ArrayList<>();
    }

    public avm_CompoundProperty(
        ArrayList<avm_PrimitiveProperty> avm_primitivepropertys,        ArrayList<avm_CompoundProperty> avm_compoundpropertys    ) {
        this.avm_primitivepropertys = avm_primitivepropertys;
        this.avm_compoundpropertys = avm_compoundpropertys;
    }


    public List<avm_PrimitiveProperty> getAvm_primitivepropertys() {
        return avm_primitivepropertys;
    }

    public void addAvm_primitiveproperty(Avm_primitiveproperty avm_primitiveproperty) {
        this.avm_primitivepropertys.add(avm_primitiveproperty);
    }
    public List<avm_CompoundProperty> getAvm_compoundpropertys() {
        return avm_compoundpropertys;
    }

    public void addAvm_compoundproperty(Avm_compoundproperty avm_compoundproperty) {
        this.avm_compoundpropertys.add(avm_compoundproperty);
    }

}