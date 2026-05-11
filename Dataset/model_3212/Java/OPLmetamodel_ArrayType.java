





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_ArrayType extends DefinedType {






    private List<OPLmetamodel_DataRef> oplmetamodel_datarefs;




    private OPLmetamodel_AbstractType oplmetamodel_abstracttype;


    public OPLmetamodel_ArrayType(
    ) {
        super(
        );
        this.oplmetamodel_datarefs = new ArrayList<>();
    }

    public OPLmetamodel_ArrayType(
        ArrayList<OPLmetamodel_DataRef> oplmetamodel_datarefs    ) {
        this.oplmetamodel_datarefs = oplmetamodel_datarefs;
    }


    public List<OPLmetamodel_DataRef> getOplmetamodel_datarefs() {
        return oplmetamodel_datarefs;
    }

    public void addOplmetamodel_dataref(Oplmetamodel_dataref oplmetamodel_dataref) {
        this.oplmetamodel_datarefs.add(oplmetamodel_dataref);
    }
    public OPLmetamodel_AbstractType getOplmetamodel_abstracttype() {
        return oplmetamodel_abstracttype;
    }

    public void setOplmetamodel_abstracttype(OPLmetamodel_AbstractType oplmetamodel_abstracttype) {
        this.oplmetamodel_abstracttype = oplmetamodel_abstracttype;
    }

}