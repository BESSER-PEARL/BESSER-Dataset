





import java.util.List;
import java.util.ArrayList;

public class idl_ScopedName extends SwitchTypeSpec, PrimaryExpr, SimpleTypeSpec, ConstType, ParamTypeSpec {

    private String name;





    private idl_UsesDcl idl_usesdcl;




    private idl_TemplateModuleInst idl_templatemoduleinst;




    private idl_ComponentDecl idl_componentdecl;




    private idl_PortDecl idl_portdecl;




    private idl_TemplateModuleRef idl_templatemoduleref;




    private idl_EmitDcl idl_emitdcl;




    private idl_ComponentDecl idl_componentdecl;




    private idl_Interface_header idl_interface_header;




    private idl_ProvidesDcl idl_providesdcl;




    private idl_HomeDecl idl_homedecl;




    private idl_ConsumesDcl idl_consumesdcl;




    private idl_ExceptionList idl_exceptionlist;




    private idl_HomeDecl idl_homedecl;




    private idl_PublishesDcl idl_publishesdcl;




    private idl_HomeDecl idl_homedecl;


    public idl_ScopedName(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public idl_UsesDcl getIdl_usesdcl() {
        return idl_usesdcl;
    }

    public void setIdl_usesdcl(idl_UsesDcl idl_usesdcl) {
        this.idl_usesdcl = idl_usesdcl;
    }
    public idl_TemplateModuleInst getIdl_templatemoduleinst() {
        return idl_templatemoduleinst;
    }

    public void setIdl_templatemoduleinst(idl_TemplateModuleInst idl_templatemoduleinst) {
        this.idl_templatemoduleinst = idl_templatemoduleinst;
    }
    public idl_ComponentDecl getIdl_componentdecl() {
        return idl_componentdecl;
    }

    public void setIdl_componentdecl(idl_ComponentDecl idl_componentdecl) {
        this.idl_componentdecl = idl_componentdecl;
    }
    public idl_PortDecl getIdl_portdecl() {
        return idl_portdecl;
    }

    public void setIdl_portdecl(idl_PortDecl idl_portdecl) {
        this.idl_portdecl = idl_portdecl;
    }
    public idl_TemplateModuleRef getIdl_templatemoduleref() {
        return idl_templatemoduleref;
    }

    public void setIdl_templatemoduleref(idl_TemplateModuleRef idl_templatemoduleref) {
        this.idl_templatemoduleref = idl_templatemoduleref;
    }
    public idl_EmitDcl getIdl_emitdcl() {
        return idl_emitdcl;
    }

    public void setIdl_emitdcl(idl_EmitDcl idl_emitdcl) {
        this.idl_emitdcl = idl_emitdcl;
    }
    public idl_ComponentDecl getIdl_componentdecl() {
        return idl_componentdecl;
    }

    public void setIdl_componentdecl(idl_ComponentDecl idl_componentdecl) {
        this.idl_componentdecl = idl_componentdecl;
    }
    public idl_Interface_header getIdl_interface_header() {
        return idl_interface_header;
    }

    public void setIdl_interface_header(idl_Interface_header idl_interface_header) {
        this.idl_interface_header = idl_interface_header;
    }
    public idl_ProvidesDcl getIdl_providesdcl() {
        return idl_providesdcl;
    }

    public void setIdl_providesdcl(idl_ProvidesDcl idl_providesdcl) {
        this.idl_providesdcl = idl_providesdcl;
    }
    public idl_HomeDecl getIdl_homedecl() {
        return idl_homedecl;
    }

    public void setIdl_homedecl(idl_HomeDecl idl_homedecl) {
        this.idl_homedecl = idl_homedecl;
    }
    public idl_ConsumesDcl getIdl_consumesdcl() {
        return idl_consumesdcl;
    }

    public void setIdl_consumesdcl(idl_ConsumesDcl idl_consumesdcl) {
        this.idl_consumesdcl = idl_consumesdcl;
    }
    public idl_ExceptionList getIdl_exceptionlist() {
        return idl_exceptionlist;
    }

    public void setIdl_exceptionlist(idl_ExceptionList idl_exceptionlist) {
        this.idl_exceptionlist = idl_exceptionlist;
    }
    public idl_HomeDecl getIdl_homedecl() {
        return idl_homedecl;
    }

    public void setIdl_homedecl(idl_HomeDecl idl_homedecl) {
        this.idl_homedecl = idl_homedecl;
    }
    public idl_PublishesDcl getIdl_publishesdcl() {
        return idl_publishesdcl;
    }

    public void setIdl_publishesdcl(idl_PublishesDcl idl_publishesdcl) {
        this.idl_publishesdcl = idl_publishesdcl;
    }
    public idl_HomeDecl getIdl_homedecl() {
        return idl_homedecl;
    }

    public void setIdl_homedecl(idl_HomeDecl idl_homedecl) {
        this.idl_homedecl = idl_homedecl;
    }

}