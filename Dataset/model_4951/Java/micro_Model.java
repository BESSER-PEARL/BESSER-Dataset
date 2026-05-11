





import java.util.List;
import java.util.ArrayList;

public class micro_Model extends NamedElement {






    private micro_PrimitiveTypeAttribute micro_primitivetypeattribute;




    private micro_Info micro_info;




    private micro_Operation micro_operation;




    private micro_AggregateService micro_aggregateservice;




    private micro_ReferenceAttribute micro_referenceattribute;


    public micro_Model(
    ) {
        super(
        );
    }



    public micro_PrimitiveTypeAttribute getMicro_primitivetypeattribute() {
        return micro_primitivetypeattribute;
    }

    public void setMicro_primitivetypeattribute(micro_PrimitiveTypeAttribute micro_primitivetypeattribute) {
        this.micro_primitivetypeattribute = micro_primitivetypeattribute;
    }
    public micro_Info getMicro_info() {
        return micro_info;
    }

    public void setMicro_info(micro_Info micro_info) {
        this.micro_info = micro_info;
    }
    public micro_Operation getMicro_operation() {
        return micro_operation;
    }

    public void setMicro_operation(micro_Operation micro_operation) {
        this.micro_operation = micro_operation;
    }
    public micro_AggregateService getMicro_aggregateservice() {
        return micro_aggregateservice;
    }

    public void setMicro_aggregateservice(micro_AggregateService micro_aggregateservice) {
        this.micro_aggregateservice = micro_aggregateservice;
    }
    public micro_ReferenceAttribute getMicro_referenceattribute() {
        return micro_referenceattribute;
    }

    public void setMicro_referenceattribute(micro_ReferenceAttribute micro_referenceattribute) {
        this.micro_referenceattribute = micro_referenceattribute;
    }

}