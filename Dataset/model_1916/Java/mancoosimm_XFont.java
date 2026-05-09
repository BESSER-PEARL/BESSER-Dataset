





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_XFont extends NamedElement {






    private List<mancoosimm_File> mancoosimm_files;


    public mancoosimm_XFont(
    ) {
        super(
        );
        this.mancoosimm_files = new ArrayList<>();
    }

    public mancoosimm_XFont(
        ArrayList<mancoosimm_File> mancoosimm_files    ) {
        this.mancoosimm_files = mancoosimm_files;
    }


    public List<mancoosimm_File> getMancoosimm_files() {
        return mancoosimm_files;
    }

    public void addMancoosimm_file(Mancoosimm_file mancoosimm_file) {
        this.mancoosimm_files.add(mancoosimm_file);
    }

}