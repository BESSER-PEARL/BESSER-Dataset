





import java.util.List;
import java.util.ArrayList;

public class ir_TypeActor extends Type {

    private String name;
    private String namespace;





    private ir_AbstractActor ir_abstractactor;


    public ir_TypeActor(
        String name,        String namespace    ) {
        super(
        );
        this.name = name;
        this.namespace = namespace;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }

    public ir_AbstractActor getIr_abstractactor() {
        return ir_abstractactor;
    }

    public void setIr_abstractactor(ir_AbstractActor ir_abstractactor) {
        this.ir_abstractactor = ir_abstractactor;
    }

}