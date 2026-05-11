





import java.util.List;
import java.util.ArrayList;

public class datamodel_SliceRepository  {






    private datamodel_Slice datamodel_slice;




    private List<datamodel_Slice> datamodel_slices;




    private datamodel_Ensemble datamodel_ensemble;


    public datamodel_SliceRepository(
    ) {
        this.datamodel_slices = new ArrayList<>();
    }

    public datamodel_SliceRepository(
        ArrayList<datamodel_Slice> datamodel_slices    ) {
        this.datamodel_slices = datamodel_slices;
    }


    public datamodel_Slice getDatamodel_slice() {
        return datamodel_slice;
    }

    public void setDatamodel_slice(datamodel_Slice datamodel_slice) {
        this.datamodel_slice = datamodel_slice;
    }
    public List<datamodel_Slice> getDatamodel_slices() {
        return datamodel_slices;
    }

    public void addDatamodel_slice(Datamodel_slice datamodel_slice) {
        this.datamodel_slices.add(datamodel_slice);
    }
    public datamodel_Ensemble getDatamodel_ensemble() {
        return datamodel_ensemble;
    }

    public void setDatamodel_ensemble(datamodel_Ensemble datamodel_ensemble) {
        this.datamodel_ensemble = datamodel_ensemble;
    }

}