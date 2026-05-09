





import java.util.List;
import java.util.ArrayList;

public class ocl_dm_EDataModel  {






    private List<EEntity> eentitys;


    public ocl_dm_EDataModel(
    ) {
        this.eentitys = new ArrayList<>();
    }

    public ocl_dm_EDataModel(
        ArrayList<EEntity> eentitys    ) {
        this.eentitys = eentitys;
    }


    public List<EEntity> getEentitys() {
        return eentitys;
    }

    public void addEentity(Eentity eentity) {
        this.eentitys.add(eentity);
    }

}