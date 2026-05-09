





import java.util.List;
import java.util.ArrayList;

public class dsl_AllocationExpression  {

    private String primType;





    private dsl_Arguments dsl_arguments;




    private dsl_TypeArguments dsl_typearguments;




    private dsl_PrimaryPrefix dsl_primaryprefix;




    private dsl_ClassOrInterfaceBody dsl_classorinterfacebody;




    private dsl_ClassOrInterfaceType dsl_classorinterfacetype;


    public dsl_AllocationExpression(
        String primType    ) {
        this.primType = primType;
    }


    public String getPrimtype() {
        return primType;
    }

    public void setPrimtype(String primType) {
        this.primType = primType;
    }

    public dsl_Arguments getDsl_arguments() {
        return dsl_arguments;
    }

    public void setDsl_arguments(dsl_Arguments dsl_arguments) {
        this.dsl_arguments = dsl_arguments;
    }
    public dsl_TypeArguments getDsl_typearguments() {
        return dsl_typearguments;
    }

    public void setDsl_typearguments(dsl_TypeArguments dsl_typearguments) {
        this.dsl_typearguments = dsl_typearguments;
    }
    public dsl_PrimaryPrefix getDsl_primaryprefix() {
        return dsl_primaryprefix;
    }

    public void setDsl_primaryprefix(dsl_PrimaryPrefix dsl_primaryprefix) {
        this.dsl_primaryprefix = dsl_primaryprefix;
    }
    public dsl_ClassOrInterfaceBody getDsl_classorinterfacebody() {
        return dsl_classorinterfacebody;
    }

    public void setDsl_classorinterfacebody(dsl_ClassOrInterfaceBody dsl_classorinterfacebody) {
        this.dsl_classorinterfacebody = dsl_classorinterfacebody;
    }
    public dsl_ClassOrInterfaceType getDsl_classorinterfacetype() {
        return dsl_classorinterfacetype;
    }

    public void setDsl_classorinterfacetype(dsl_ClassOrInterfaceType dsl_classorinterfacetype) {
        this.dsl_classorinterfacetype = dsl_classorinterfacetype;
    }

}