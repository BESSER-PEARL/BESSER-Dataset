





import java.util.List;
import java.util.ArrayList;

public class HSM_StateBase extends MgaObject {

    private String defaultTransition;
    private String marked;





    private AssociationDataStateBase associationdatastatebase;




    private List<DataVar> datavars;


    public HSM_StateBase(
        String defaultTransition,        String marked    ) {
        super(
        );
        this.defaultTransition = defaultTransition;
        this.marked = marked;
        this.datavars = new ArrayList<>();
    }

    public HSM_StateBase(
        String defaultTransition,        String marked        ArrayList<DataVar> datavars    ) {
        this.defaultTransition = defaultTransition;
        this.marked = marked;
        this.datavars = datavars;
    }

    public String getDefaulttransition() {
        return defaultTransition;
    }

    public void setDefaulttransition(String defaultTransition) {
        this.defaultTransition = defaultTransition;
    }
    public String getMarked() {
        return marked;
    }

    public void setMarked(String marked) {
        this.marked = marked;
    }

    public AssociationDataStateBase getAssociationdatastatebase() {
        return associationdatastatebase;
    }

    public void setAssociationdatastatebase(AssociationDataStateBase associationdatastatebase) {
        this.associationdatastatebase = associationdatastatebase;
    }
    public List<DataVar> getDatavars() {
        return datavars;
    }

    public void addDatavar(Datavar datavar) {
        this.datavars.add(datavar);
    }

}