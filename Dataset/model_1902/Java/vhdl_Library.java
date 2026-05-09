





import java.util.List;
import java.util.ArrayList;

public class vhdl_Library  {

    private String builtin_lib;





    private vhdl_EntityInstantiationStatement vhdl_entityinstantiationstatement;




    private vhdl_LibraryClause vhdl_libraryclause;




    private vhdl_UseClause vhdl_useclause;


    public vhdl_Library(
        String builtin_lib    ) {
        this.builtin_lib = builtin_lib;
    }


    public String getBuiltin_lib() {
        return builtin_lib;
    }

    public void setBuiltin_lib(String builtin_lib) {
        this.builtin_lib = builtin_lib;
    }

    public vhdl_EntityInstantiationStatement getVhdl_entityinstantiationstatement() {
        return vhdl_entityinstantiationstatement;
    }

    public void setVhdl_entityinstantiationstatement(vhdl_EntityInstantiationStatement vhdl_entityinstantiationstatement) {
        this.vhdl_entityinstantiationstatement = vhdl_entityinstantiationstatement;
    }
    public vhdl_LibraryClause getVhdl_libraryclause() {
        return vhdl_libraryclause;
    }

    public void setVhdl_libraryclause(vhdl_LibraryClause vhdl_libraryclause) {
        this.vhdl_libraryclause = vhdl_libraryclause;
    }
    public vhdl_UseClause getVhdl_useclause() {
        return vhdl_useclause;
    }

    public void setVhdl_useclause(vhdl_UseClause vhdl_useclause) {
        this.vhdl_useclause = vhdl_useclause;
    }

}