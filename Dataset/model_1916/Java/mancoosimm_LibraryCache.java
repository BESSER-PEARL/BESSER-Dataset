





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_LibraryCache  {






    private mancoosimm_Environment mancoosimm_environment;




    private List<mancoosimm_File> mancoosimm_files;




    private mancoosimm_Environment mancoosimm_environment;


    public mancoosimm_LibraryCache(
    ) {
        this.mancoosimm_files = new ArrayList<>();
    }

    public mancoosimm_LibraryCache(
        ArrayList<mancoosimm_File> mancoosimm_files    ) {
        this.mancoosimm_files = mancoosimm_files;
    }


    public mancoosimm_Environment getMancoosimm_environment() {
        return mancoosimm_environment;
    }

    public void setMancoosimm_environment(mancoosimm_Environment mancoosimm_environment) {
        this.mancoosimm_environment = mancoosimm_environment;
    }
    public List<mancoosimm_File> getMancoosimm_files() {
        return mancoosimm_files;
    }

    public void addMancoosimm_file(Mancoosimm_file mancoosimm_file) {
        this.mancoosimm_files.add(mancoosimm_file);
    }
    public mancoosimm_Environment getMancoosimm_environment() {
        return mancoosimm_environment;
    }

    public void setMancoosimm_environment(mancoosimm_Environment mancoosimm_environment) {
        this.mancoosimm_environment = mancoosimm_environment;
    }

}