





import java.util.List;
import java.util.ArrayList;

public class qsar_DescriptorresultType  {

    private String structureid;
    private String errorString;
    private String descriptorid;





    private qsar_DescriptorresultlistsType qsar_descriptorresultliststype;


    public qsar_DescriptorresultType(
        String structureid,        String errorString,        String descriptorid    ) {
        this.structureid = structureid;
        this.errorString = errorString;
        this.descriptorid = descriptorid;
    }


    public String getStructureid() {
        return structureid;
    }

    public void setStructureid(String structureid) {
        this.structureid = structureid;
    }
    public String getErrorstring() {
        return errorString;
    }

    public void setErrorstring(String errorString) {
        this.errorString = errorString;
    }
    public String getDescriptorid() {
        return descriptorid;
    }

    public void setDescriptorid(String descriptorid) {
        this.descriptorid = descriptorid;
    }

    public qsar_DescriptorresultlistsType getQsar_descriptorresultliststype() {
        return qsar_descriptorresultliststype;
    }

    public void setQsar_descriptorresultliststype(qsar_DescriptorresultlistsType qsar_descriptorresultliststype) {
        this.qsar_descriptorresultliststype = qsar_descriptorresultliststype;
    }

}