





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_Sequence  {






    private List<OPLmetamodel_Interval> oplmetamodel_intervals;




    private OPLmetamodel_DefinedType oplmetamodel_definedtype;


    public OPLmetamodel_Sequence(
    ) {
        this.oplmetamodel_intervals = new ArrayList<>();
    }

    public OPLmetamodel_Sequence(
        ArrayList<OPLmetamodel_Interval> oplmetamodel_intervals    ) {
        this.oplmetamodel_intervals = oplmetamodel_intervals;
    }


    public List<OPLmetamodel_Interval> getOplmetamodel_intervals() {
        return oplmetamodel_intervals;
    }

    public void addOplmetamodel_interval(Oplmetamodel_interval oplmetamodel_interval) {
        this.oplmetamodel_intervals.add(oplmetamodel_interval);
    }
    public OPLmetamodel_DefinedType getOplmetamodel_definedtype() {
        return oplmetamodel_definedtype;
    }

    public void setOplmetamodel_definedtype(OPLmetamodel_DefinedType oplmetamodel_definedtype) {
        this.oplmetamodel_definedtype = oplmetamodel_definedtype;
    }

}