





import java.util.List;
import java.util.ArrayList;

public class ir_VariableImport extends Declaration {

    private String namespace;



    public ir_VariableImport(
        String namespace    ) {
        super(
        );
        this.namespace = namespace;
    }


    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }


}