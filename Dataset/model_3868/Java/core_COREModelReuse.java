





import java.util.List;
import java.util.ArrayList;

public class core_COREModelReuse  {






    private core_COREModel core_coremodel;




    private List<core_COREReuse> core_corereuses;


    public core_COREModelReuse(
    ) {
        this.core_corereuses = new ArrayList<>();
    }

    public core_COREModelReuse(
        ArrayList<core_COREReuse> core_corereuses    ) {
        this.core_corereuses = core_corereuses;
    }


    public core_COREModel getCore_coremodel() {
        return core_coremodel;
    }

    public void setCore_coremodel(core_COREModel core_coremodel) {
        this.core_coremodel = core_coremodel;
    }
    public List<core_COREReuse> getCore_corereuses() {
        return core_corereuses;
    }

    public void addCore_corereuse(Core_corereuse core_corereuse) {
        this.core_corereuses.add(core_corereuse);
    }

}