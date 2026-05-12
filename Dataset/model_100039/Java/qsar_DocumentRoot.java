





import java.util.List;
import java.util.ArrayList;

public class qsar_DocumentRoot  {

    private String mixed;





    private List<qsar_QsarType> qsar_qsartypes;


    public qsar_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.qsar_qsartypes = new ArrayList<>();
    }

    public qsar_DocumentRoot(
        String mixed        ArrayList<qsar_QsarType> qsar_qsartypes    ) {
        this.mixed = mixed;
        this.qsar_qsartypes = qsar_qsartypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<qsar_QsarType> getQsar_qsartypes() {
        return qsar_qsartypes;
    }

    public void addQsar_qsartype(Qsar_qsartype qsar_qsartype) {
        this.qsar_qsartypes.add(qsar_qsartype);
    }

}