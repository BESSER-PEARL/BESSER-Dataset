





import java.util.List;
import java.util.ArrayList;

public class ISO20022_LogicalType extends Type {






    private ISO20022_LogicalType iso20022_logicaltype;




    private List<ISO20022_LogicalType> iso20022_logicaltypes;


    public ISO20022_LogicalType(
    ) {
        super(
        );
        this.iso20022_logicaltypes = new ArrayList<>();
    }

    public ISO20022_LogicalType(
        ArrayList<ISO20022_LogicalType> iso20022_logicaltypes    ) {
        this.iso20022_logicaltypes = iso20022_logicaltypes;
    }


    public ISO20022_LogicalType getIso20022_logicaltype() {
        return iso20022_logicaltype;
    }

    public void setIso20022_logicaltype(ISO20022_LogicalType iso20022_logicaltype) {
        this.iso20022_logicaltype = iso20022_logicaltype;
    }
    public List<ISO20022_LogicalType> getIso20022_logicaltypes() {
        return iso20022_logicaltypes;
    }

    public void addIso20022_logicaltype(Iso20022_logicaltype iso20022_logicaltype) {
        this.iso20022_logicaltypes.add(iso20022_logicaltype);
    }

}