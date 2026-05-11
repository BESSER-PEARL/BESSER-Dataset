





import java.util.List;
import java.util.ArrayList;

public class xpdl2_DataTypeType  {

    private String carnotType;





    private xpdl2_BasicTypeType xpdl2_basictypetype;




    private xpdl2_DeclaredTypeType xpdl2_declaredtypetype;




    private xpdl2_ExternalReferenceType xpdl2_externalreferencetype;




    private xpdl2_SchemaTypeType xpdl2_schematypetype;


    public xpdl2_DataTypeType(
        String carnotType    ) {
        this.carnotType = carnotType;
    }


    public String getCarnottype() {
        return carnotType;
    }

    public void setCarnottype(String carnotType) {
        this.carnotType = carnotType;
    }

    public xpdl2_BasicTypeType getXpdl2_basictypetype() {
        return xpdl2_basictypetype;
    }

    public void setXpdl2_basictypetype(xpdl2_BasicTypeType xpdl2_basictypetype) {
        this.xpdl2_basictypetype = xpdl2_basictypetype;
    }
    public xpdl2_DeclaredTypeType getXpdl2_declaredtypetype() {
        return xpdl2_declaredtypetype;
    }

    public void setXpdl2_declaredtypetype(xpdl2_DeclaredTypeType xpdl2_declaredtypetype) {
        this.xpdl2_declaredtypetype = xpdl2_declaredtypetype;
    }
    public xpdl2_ExternalReferenceType getXpdl2_externalreferencetype() {
        return xpdl2_externalreferencetype;
    }

    public void setXpdl2_externalreferencetype(xpdl2_ExternalReferenceType xpdl2_externalreferencetype) {
        this.xpdl2_externalreferencetype = xpdl2_externalreferencetype;
    }
    public xpdl2_SchemaTypeType getXpdl2_schematypetype() {
        return xpdl2_schematypetype;
    }

    public void setXpdl2_schematypetype(xpdl2_SchemaTypeType xpdl2_schematypetype) {
        this.xpdl2_schematypetype = xpdl2_schematypetype;
    }

}