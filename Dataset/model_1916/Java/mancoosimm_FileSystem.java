





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_FileSystem extends NamedElement {






    private mancoosimm_Configuration mancoosimm_configuration;




    private mancoosimm_Configuration mancoosimm_configuration;




    private List<mancoosimm_File> mancoosimm_files;




    private mancoosimm_File mancoosimm_file;




    private mancoosimm_File mancoosimm_file;


    public mancoosimm_FileSystem(
    ) {
        super(
        );
        this.mancoosimm_files = new ArrayList<>();
    }

    public mancoosimm_FileSystem(
        ArrayList<mancoosimm_File> mancoosimm_files    ) {
        this.mancoosimm_files = mancoosimm_files;
    }


    public mancoosimm_Configuration getMancoosimm_configuration() {
        return mancoosimm_configuration;
    }

    public void setMancoosimm_configuration(mancoosimm_Configuration mancoosimm_configuration) {
        this.mancoosimm_configuration = mancoosimm_configuration;
    }
    public mancoosimm_Configuration getMancoosimm_configuration() {
        return mancoosimm_configuration;
    }

    public void setMancoosimm_configuration(mancoosimm_Configuration mancoosimm_configuration) {
        this.mancoosimm_configuration = mancoosimm_configuration;
    }
    public List<mancoosimm_File> getMancoosimm_files() {
        return mancoosimm_files;
    }

    public void addMancoosimm_file(Mancoosimm_file mancoosimm_file) {
        this.mancoosimm_files.add(mancoosimm_file);
    }
    public mancoosimm_File getMancoosimm_file() {
        return mancoosimm_file;
    }

    public void setMancoosimm_file(mancoosimm_File mancoosimm_file) {
        this.mancoosimm_file = mancoosimm_file;
    }
    public mancoosimm_File getMancoosimm_file() {
        return mancoosimm_file;
    }

    public void setMancoosimm_file(mancoosimm_File mancoosimm_file) {
        this.mancoosimm_file = mancoosimm_file;
    }

}