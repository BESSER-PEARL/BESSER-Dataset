





import java.util.List;
import java.util.ArrayList;

public class adb_UseTypeClause extends UseClause {

    private String useTypeRefs;
    private String typesNames;



    public adb_UseTypeClause(
        String useTypeRefs,        String typesNames    ) {
        super(
        );
        this.useTypeRefs = useTypeRefs;
        this.typesNames = typesNames;
    }


    public String getUsetyperefs() {
        return useTypeRefs;
    }

    public void setUsetyperefs(String useTypeRefs) {
        this.useTypeRefs = useTypeRefs;
    }
    public String getTypesnames() {
        return typesNames;
    }

    public void setTypesnames(String typesNames) {
        this.typesNames = typesNames;
    }


}