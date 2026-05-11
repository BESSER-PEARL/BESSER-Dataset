





import java.util.List;
import java.util.ArrayList;

public class etricegen_Root  {

    private boolean library;





    private List<etricegen_SystemInstance> etricegen_systeminstances;


    public etricegen_Root(
        boolean library    ) {
        this.library = library;
        this.etricegen_systeminstances = new ArrayList<>();
    }

    public etricegen_Root(
        boolean library        ArrayList<etricegen_SystemInstance> etricegen_systeminstances    ) {
        this.library = library;
        this.etricegen_systeminstances = etricegen_systeminstances;
    }

    public boolean getLibrary() {
        return library;
    }

    public void setLibrary(boolean library) {
        this.library = library;
    }

    public List<etricegen_SystemInstance> getEtricegen_systeminstances() {
        return etricegen_systeminstances;
    }

    public void addEtricegen_systeminstance(Etricegen_systeminstance etricegen_systeminstance) {
        this.etricegen_systeminstances.add(etricegen_systeminstance);
    }

}