





import java.util.List;
import java.util.ArrayList;

public class Type  {






    private OCL_Package ocl_package;




    private OCL_TypedElement ocl_typedelement;




    private OCL_CollectionType ocl_collectiontype;




    private OCL_Operation ocl_operation;


    public Type(
    ) {
    }



    public OCL_Package getOcl_package() {
        return ocl_package;
    }

    public void setOcl_package(OCL_Package ocl_package) {
        this.ocl_package = ocl_package;
    }
    public OCL_TypedElement getOcl_typedelement() {
        return ocl_typedelement;
    }

    public void setOcl_typedelement(OCL_TypedElement ocl_typedelement) {
        this.ocl_typedelement = ocl_typedelement;
    }
    public OCL_CollectionType getOcl_collectiontype() {
        return ocl_collectiontype;
    }

    public void setOcl_collectiontype(OCL_CollectionType ocl_collectiontype) {
        this.ocl_collectiontype = ocl_collectiontype;
    }
    public OCL_Operation getOcl_operation() {
        return ocl_operation;
    }

    public void setOcl_operation(OCL_Operation ocl_operation) {
        this.ocl_operation = ocl_operation;
    }

}