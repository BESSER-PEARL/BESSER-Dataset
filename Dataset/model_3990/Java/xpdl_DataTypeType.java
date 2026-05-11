





import java.util.List;
import java.util.ArrayList;

public class xpdl_DataTypeType  {

    private String carnotType;





    private xpdl_DeclaredTypeType xpdl_declaredtypetype;




    private xpdl_ExternalReferenceType xpdl_externalreferencetype;




    private xpdl_SchemaTypeType xpdl_schematypetype;




    private xpdl_BasicTypeType xpdl_basictypetype;


    public xpdl_DataTypeType(
        String carnotType    ) {
        this.carnotType = carnotType;
    }


    public String getCarnottype() {
        return carnotType;
    }

    public void setCarnottype(String carnotType) {
        this.carnotType = carnotType;
    }

    public xpdl_DeclaredTypeType getXpdl_declaredtypetype() {
        return xpdl_declaredtypetype;
    }

    public void setXpdl_declaredtypetype(xpdl_DeclaredTypeType xpdl_declaredtypetype) {
        this.xpdl_declaredtypetype = xpdl_declaredtypetype;
    }
    public xpdl_ExternalReferenceType getXpdl_externalreferencetype() {
        return xpdl_externalreferencetype;
    }

    public void setXpdl_externalreferencetype(xpdl_ExternalReferenceType xpdl_externalreferencetype) {
        this.xpdl_externalreferencetype = xpdl_externalreferencetype;
    }
    public xpdl_SchemaTypeType getXpdl_schematypetype() {
        return xpdl_schematypetype;
    }

    public void setXpdl_schematypetype(xpdl_SchemaTypeType xpdl_schematypetype) {
        this.xpdl_schematypetype = xpdl_schematypetype;
    }
    public xpdl_BasicTypeType getXpdl_basictypetype() {
        return xpdl_basictypetype;
    }

    public void setXpdl_basictypetype(xpdl_BasicTypeType xpdl_basictypetype) {
        this.xpdl_basictypetype = xpdl_basictypetype;
    }

}