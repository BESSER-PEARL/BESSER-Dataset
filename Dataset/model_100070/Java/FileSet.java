





import java.util.List;
import java.util.ArrayList;

public class FileSet  {






    private Ant_ClassPath ant_classpath;




    private Ant_Path ant_path;




    private Ant_Copy ant_copy;


    public FileSet(
    ) {
    }



    public Ant_ClassPath getAnt_classpath() {
        return ant_classpath;
    }

    public void setAnt_classpath(Ant_ClassPath ant_classpath) {
        this.ant_classpath = ant_classpath;
    }
    public Ant_Path getAnt_path() {
        return ant_path;
    }

    public void setAnt_path(Ant_Path ant_path) {
        this.ant_path = ant_path;
    }
    public Ant_Copy getAnt_copy() {
        return ant_copy;
    }

    public void setAnt_copy(Ant_Copy ant_copy) {
        this.ant_copy = ant_copy;
    }

}