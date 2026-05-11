





import java.util.List;
import java.util.ArrayList;

public class vql_AggregatedValue extends ComputationValue {






    private vql_JvmDeclaredType vql_jvmdeclaredtype;




    private vql_CallableRelation vql_callablerelation;


    public vql_AggregatedValue(
    ) {
        super(
        );
    }



    public vql_JvmDeclaredType getVql_jvmdeclaredtype() {
        return vql_jvmdeclaredtype;
    }

    public void setVql_jvmdeclaredtype(vql_JvmDeclaredType vql_jvmdeclaredtype) {
        this.vql_jvmdeclaredtype = vql_jvmdeclaredtype;
    }
    public vql_CallableRelation getVql_callablerelation() {
        return vql_callablerelation;
    }

    public void setVql_callablerelation(vql_CallableRelation vql_callablerelation) {
        this.vql_callablerelation = vql_callablerelation;
    }

}