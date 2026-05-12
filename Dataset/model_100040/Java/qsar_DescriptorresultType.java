





import java.util.List;
import java.util.ArrayList;

public class qsar_DescriptorresultType  {

    private String descriptorid;
    private String structureid;





    private qsar_DescriptorresultlistsType qsar_descriptorresultliststype;


    public qsar_DescriptorresultType(
        String descriptorid,        String structureid    ) {
        this.descriptorid = descriptorid;
        this.structureid = structureid;
    }


    public String getDescriptorid() {
        return descriptorid;
    }

    public void setDescriptorid(String descriptorid) {
        this.descriptorid = descriptorid;
    }
    public String getStructureid() {
        return structureid;
    }

    public void setStructureid(String structureid) {
        this.structureid = structureid;
    }

    public qsar_DescriptorresultlistsType getQsar_descriptorresultliststype() {
        return qsar_descriptorresultliststype;
    }

    public void setQsar_descriptorresultliststype(qsar_DescriptorresultlistsType qsar_descriptorresultliststype) {
        this.qsar_descriptorresultliststype = qsar_descriptorresultliststype;
    }

}