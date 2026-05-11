





import java.util.List;
import java.util.ArrayList;

public class idl_IDLComment extends ComponentExport, PortExport, Export, TemplateDefinition, Definition, ConnectorExport, FixedDefinition {

    private String body;





    private idl_PortTypeDecl idl_porttypedecl;




    private idl_HomeDecl idl_homedecl;




    private idl_ComponentDecl idl_componentdecl;




    private idl_StructType idl_structtype;




    private idl_ConstDecl idl_constdecl;




    private idl_Module idl_module;


    public idl_IDLComment(
        String body    ) {
        super(
        );
        this.body = body;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public idl_PortTypeDecl getIdl_porttypedecl() {
        return idl_porttypedecl;
    }

    public void setIdl_porttypedecl(idl_PortTypeDecl idl_porttypedecl) {
        this.idl_porttypedecl = idl_porttypedecl;
    }
    public idl_HomeDecl getIdl_homedecl() {
        return idl_homedecl;
    }

    public void setIdl_homedecl(idl_HomeDecl idl_homedecl) {
        this.idl_homedecl = idl_homedecl;
    }
    public idl_ComponentDecl getIdl_componentdecl() {
        return idl_componentdecl;
    }

    public void setIdl_componentdecl(idl_ComponentDecl idl_componentdecl) {
        this.idl_componentdecl = idl_componentdecl;
    }
    public idl_StructType getIdl_structtype() {
        return idl_structtype;
    }

    public void setIdl_structtype(idl_StructType idl_structtype) {
        this.idl_structtype = idl_structtype;
    }
    public idl_ConstDecl getIdl_constdecl() {
        return idl_constdecl;
    }

    public void setIdl_constdecl(idl_ConstDecl idl_constdecl) {
        this.idl_constdecl = idl_constdecl;
    }
    public idl_Module getIdl_module() {
        return idl_module;
    }

    public void setIdl_module(idl_Module idl_module) {
        this.idl_module = idl_module;
    }

}