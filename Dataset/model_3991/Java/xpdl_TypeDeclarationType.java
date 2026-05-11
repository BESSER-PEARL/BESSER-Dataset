





import java.util.List;
import java.util.ArrayList;

public class xpdl_TypeDeclarationType extends Extensible {

    private String description;
    private String id;
    private String name;





    private xpdl_SchemaTypeType xpdl_schematypetype;




    private xpdl_DeclaredTypeType xpdl_declaredtypetype;




    private xpdl_BasicTypeType xpdl_basictypetype;




    private xpdl_ExternalReferenceType xpdl_externalreferencetype;


    public xpdl_TypeDeclarationType(
        String description,        String id,        String name    ) {
        super(
        );
        this.description = description;
        this.id = id;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public xpdl_SchemaTypeType getXpdl_schematypetype() {
        return xpdl_schematypetype;
    }

    public void setXpdl_schematypetype(xpdl_SchemaTypeType xpdl_schematypetype) {
        this.xpdl_schematypetype = xpdl_schematypetype;
    }
    public xpdl_DeclaredTypeType getXpdl_declaredtypetype() {
        return xpdl_declaredtypetype;
    }

    public void setXpdl_declaredtypetype(xpdl_DeclaredTypeType xpdl_declaredtypetype) {
        this.xpdl_declaredtypetype = xpdl_declaredtypetype;
    }
    public xpdl_BasicTypeType getXpdl_basictypetype() {
        return xpdl_basictypetype;
    }

    public void setXpdl_basictypetype(xpdl_BasicTypeType xpdl_basictypetype) {
        this.xpdl_basictypetype = xpdl_basictypetype;
    }
    public xpdl_ExternalReferenceType getXpdl_externalreferencetype() {
        return xpdl_externalreferencetype;
    }

    public void setXpdl_externalreferencetype(xpdl_ExternalReferenceType xpdl_externalreferencetype) {
        this.xpdl_externalreferencetype = xpdl_externalreferencetype;
    }

}