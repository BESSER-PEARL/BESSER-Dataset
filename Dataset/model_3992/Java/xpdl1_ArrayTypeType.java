





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ArrayTypeType  {

    private String upperIndex;
    private String lowerIndex;





    private xpdl1_RecordTypeType xpdl1_recordtypetype;




    private xpdl1_UnionTypeType xpdl1_uniontypetype;




    private xpdl1_ExternalReferenceType xpdl1_externalreferencetype;




    private xpdl1_ArrayTypeType xpdl1_arraytypetype;


    public xpdl1_ArrayTypeType(
        String upperIndex,        String lowerIndex    ) {
        this.upperIndex = upperIndex;
        this.lowerIndex = lowerIndex;
    }


    public String getUpperindex() {
        return upperIndex;
    }

    public void setUpperindex(String upperIndex) {
        this.upperIndex = upperIndex;
    }
    public String getLowerindex() {
        return lowerIndex;
    }

    public void setLowerindex(String lowerIndex) {
        this.lowerIndex = lowerIndex;
    }

    public xpdl1_RecordTypeType getXpdl1_recordtypetype() {
        return xpdl1_recordtypetype;
    }

    public void setXpdl1_recordtypetype(xpdl1_RecordTypeType xpdl1_recordtypetype) {
        this.xpdl1_recordtypetype = xpdl1_recordtypetype;
    }
    public xpdl1_UnionTypeType getXpdl1_uniontypetype() {
        return xpdl1_uniontypetype;
    }

    public void setXpdl1_uniontypetype(xpdl1_UnionTypeType xpdl1_uniontypetype) {
        this.xpdl1_uniontypetype = xpdl1_uniontypetype;
    }
    public xpdl1_ExternalReferenceType getXpdl1_externalreferencetype() {
        return xpdl1_externalreferencetype;
    }

    public void setXpdl1_externalreferencetype(xpdl1_ExternalReferenceType xpdl1_externalreferencetype) {
        this.xpdl1_externalreferencetype = xpdl1_externalreferencetype;
    }
    public xpdl1_ArrayTypeType getXpdl1_arraytypetype() {
        return xpdl1_arraytypetype;
    }

    public void setXpdl1_arraytypetype(xpdl1_ArrayTypeType xpdl1_arraytypetype) {
        this.xpdl1_arraytypetype = xpdl1_arraytypetype;
    }

}