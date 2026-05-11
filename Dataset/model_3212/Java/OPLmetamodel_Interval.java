





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_Interval  {

    private boolean isOptional;





    private OPLmetamodel_NumericType oplmetamodel_numerictype;




    private OPLmetamodel_RangeType oplmetamodel_rangetype;


    public OPLmetamodel_Interval(
        boolean isOptional    ) {
        this.isOptional = isOptional;
    }


    public boolean getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(boolean isOptional) {
        this.isOptional = isOptional;
    }

    public OPLmetamodel_NumericType getOplmetamodel_numerictype() {
        return oplmetamodel_numerictype;
    }

    public void setOplmetamodel_numerictype(OPLmetamodel_NumericType oplmetamodel_numerictype) {
        this.oplmetamodel_numerictype = oplmetamodel_numerictype;
    }
    public OPLmetamodel_RangeType getOplmetamodel_rangetype() {
        return oplmetamodel_rangetype;
    }

    public void setOplmetamodel_rangetype(OPLmetamodel_RangeType oplmetamodel_rangetype) {
        this.oplmetamodel_rangetype = oplmetamodel_rangetype;
    }

}