





import java.util.List;
import java.util.ArrayList;

public class adb_Pragma extends ContextItem, Statement, BasicDeclarativeItem {

    private String name;





    private adb_CompilationUnit adb_compilationunit;


    public adb_Pragma(
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

    public adb_CompilationUnit getAdb_compilationunit() {
        return adb_compilationunit;
    }

    public void setAdb_compilationunit(adb_CompilationUnit adb_compilationunit) {
        this.adb_compilationunit = adb_compilationunit;
    }

}