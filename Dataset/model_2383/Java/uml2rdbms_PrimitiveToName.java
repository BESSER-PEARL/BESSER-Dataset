





import java.util.List;
import java.util.ArrayList;

public class uml2rdbms_PrimitiveToName extends UmlToRdbmsModelElement {

    private String typeName;





    private uml2rdbms_PackageToSchema uml2rdbms_packagetoschema;




    private uml2rdbms_AttributeToColumn uml2rdbms_attributetocolumn;




    private uml2rdbms_PackageToSchema uml2rdbms_packagetoschema;


    public uml2rdbms_PrimitiveToName(
        String typeName    ) {
        super(
        );
        this.typeName = typeName;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }

    public uml2rdbms_PackageToSchema getUml2rdbms_packagetoschema() {
        return uml2rdbms_packagetoschema;
    }

    public void setUml2rdbms_packagetoschema(uml2rdbms_PackageToSchema uml2rdbms_packagetoschema) {
        this.uml2rdbms_packagetoschema = uml2rdbms_packagetoschema;
    }
    public uml2rdbms_AttributeToColumn getUml2rdbms_attributetocolumn() {
        return uml2rdbms_attributetocolumn;
    }

    public void setUml2rdbms_attributetocolumn(uml2rdbms_AttributeToColumn uml2rdbms_attributetocolumn) {
        this.uml2rdbms_attributetocolumn = uml2rdbms_attributetocolumn;
    }
    public uml2rdbms_PackageToSchema getUml2rdbms_packagetoschema() {
        return uml2rdbms_packagetoschema;
    }

    public void setUml2rdbms_packagetoschema(uml2rdbms_PackageToSchema uml2rdbms_packagetoschema) {
        this.uml2rdbms_packagetoschema = uml2rdbms_packagetoschema;
    }

}