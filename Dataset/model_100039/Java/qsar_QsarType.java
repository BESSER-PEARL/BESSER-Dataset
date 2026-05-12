





import java.util.List;
import java.util.ArrayList;

public class qsar_QsarType  {






    private List<qsar_DescriptorproviderType> qsar_descriptorprovidertypes;




    private qsar_DescriptorlistType qsar_descriptorlisttype;




    private qsar_ResponsesListType qsar_responseslisttype;




    private qsar_StructurelistType qsar_structurelisttype;




    private qsar_DescriptorresultlistsType qsar_descriptorresultliststype;


    public qsar_QsarType(
    ) {
        this.qsar_descriptorprovidertypes = new ArrayList<>();
    }

    public qsar_QsarType(
        ArrayList<qsar_DescriptorproviderType> qsar_descriptorprovidertypes    ) {
        this.qsar_descriptorprovidertypes = qsar_descriptorprovidertypes;
    }


    public List<qsar_DescriptorproviderType> getQsar_descriptorprovidertypes() {
        return qsar_descriptorprovidertypes;
    }

    public void addQsar_descriptorprovidertype(Qsar_descriptorprovidertype qsar_descriptorprovidertype) {
        this.qsar_descriptorprovidertypes.add(qsar_descriptorprovidertype);
    }
    public qsar_DescriptorlistType getQsar_descriptorlisttype() {
        return qsar_descriptorlisttype;
    }

    public void setQsar_descriptorlisttype(qsar_DescriptorlistType qsar_descriptorlisttype) {
        this.qsar_descriptorlisttype = qsar_descriptorlisttype;
    }
    public qsar_ResponsesListType getQsar_responseslisttype() {
        return qsar_responseslisttype;
    }

    public void setQsar_responseslisttype(qsar_ResponsesListType qsar_responseslisttype) {
        this.qsar_responseslisttype = qsar_responseslisttype;
    }
    public qsar_StructurelistType getQsar_structurelisttype() {
        return qsar_structurelisttype;
    }

    public void setQsar_structurelisttype(qsar_StructurelistType qsar_structurelisttype) {
        this.qsar_structurelisttype = qsar_structurelisttype;
    }
    public qsar_DescriptorresultlistsType getQsar_descriptorresultliststype() {
        return qsar_descriptorresultliststype;
    }

    public void setQsar_descriptorresultliststype(qsar_DescriptorresultlistsType qsar_descriptorresultliststype) {
        this.qsar_descriptorresultliststype = qsar_descriptorresultliststype;
    }

}