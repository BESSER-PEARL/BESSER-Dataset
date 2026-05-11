





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_TupleBinding  {






    private List<OPLmetamodel_BindingRef> oplmetamodel_bindingrefs;


    public OPLmetamodel_TupleBinding(
    ) {
        this.oplmetamodel_bindingrefs = new ArrayList<>();
    }

    public OPLmetamodel_TupleBinding(
        ArrayList<OPLmetamodel_BindingRef> oplmetamodel_bindingrefs    ) {
        this.oplmetamodel_bindingrefs = oplmetamodel_bindingrefs;
    }


    public List<OPLmetamodel_BindingRef> getOplmetamodel_bindingrefs() {
        return oplmetamodel_bindingrefs;
    }

    public void addOplmetamodel_bindingref(Oplmetamodel_bindingref oplmetamodel_bindingref) {
        this.oplmetamodel_bindingrefs.add(oplmetamodel_bindingref);
    }

}