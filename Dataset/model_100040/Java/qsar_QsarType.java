





import java.util.List;
import java.util.ArrayList;

public class qsar_QsarType  {






    private qsar_DescriptorresultlistsType qsar_descriptorresultliststype;




    private qsar_DocumentRoot qsar_documentroot;




    private List<qsar_DescriptorproviderType> qsar_descriptorprovidertypes;




    private qsar_DescriptorlistType qsar_descriptorlisttype;


    public qsar_QsarType(
    ) {
        this.qsar_descriptorprovidertypes = new ArrayList<>();
    }

    public qsar_QsarType(
        ArrayList<qsar_DescriptorproviderType> qsar_descriptorprovidertypes    ) {
        this.qsar_descriptorprovidertypes = qsar_descriptorprovidertypes;
    }


    public qsar_DescriptorresultlistsType getQsar_descriptorresultliststype() {
        return qsar_descriptorresultliststype;
    }

    public void setQsar_descriptorresultliststype(qsar_DescriptorresultlistsType qsar_descriptorresultliststype) {
        this.qsar_descriptorresultliststype = qsar_descriptorresultliststype;
    }
    public qsar_DocumentRoot getQsar_documentroot() {
        return qsar_documentroot;
    }

    public void setQsar_documentroot(qsar_DocumentRoot qsar_documentroot) {
        this.qsar_documentroot = qsar_documentroot;
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

}