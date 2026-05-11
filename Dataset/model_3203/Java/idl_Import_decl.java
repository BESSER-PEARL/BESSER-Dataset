





import java.util.List;
import java.util.ArrayList;

public class idl_Import_decl  {

    private String imported_scope;





    private idl_Specification idl_specification;


    public idl_Import_decl(
        String imported_scope    ) {
        this.imported_scope = imported_scope;
    }


    public String getImported_scope() {
        return imported_scope;
    }

    public void setImported_scope(String imported_scope) {
        this.imported_scope = imported_scope;
    }

    public idl_Specification getIdl_specification() {
        return idl_specification;
    }

    public void setIdl_specification(idl_Specification idl_specification) {
        this.idl_specification = idl_specification;
    }

}