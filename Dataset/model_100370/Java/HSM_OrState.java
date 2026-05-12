





import java.util.List;
import java.util.ArrayList;

public class HSM_OrState extends CompoundState {






    private RootFolder rootfolder;




    private List<DataVar> datavars;


    public HSM_OrState(
    ) {
        super(
        );
        this.datavars = new ArrayList<>();
    }

    public HSM_OrState(
        ArrayList<DataVar> datavars    ) {
        this.datavars = datavars;
    }


    public RootFolder getRootfolder() {
        return rootfolder;
    }

    public void setRootfolder(RootFolder rootfolder) {
        this.rootfolder = rootfolder;
    }
    public List<DataVar> getDatavars() {
        return datavars;
    }

    public void addDatavar(Datavar datavar) {
        this.datavars.add(datavar);
    }

}