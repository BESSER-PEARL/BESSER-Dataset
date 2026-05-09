





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_ModelElementGroup  {

    private String name;





    private List<ModelElementId> modelelementids;


    public esmodel_operations_ModelElementGroup(
        String name    ) {
        this.name = name;
        this.modelelementids = new ArrayList<>();
    }

    public esmodel_operations_ModelElementGroup(
        String name        ArrayList<ModelElementId> modelelementids    ) {
        this.name = name;
        this.modelelementids = modelelementids;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ModelElementId> getModelelementids() {
        return modelelementids;
    }

    public void addModelelementid(Modelelementid modelelementid) {
        this.modelelementids.add(modelelementid);
    }

}