





import java.util.List;
import java.util.ArrayList;

public class qsar_PreprocessingType  {






    private List<qsar_PreprocessingStepType> qsar_preprocessingsteptypes;




    private qsar_QsarType qsar_qsartype;


    public qsar_PreprocessingType(
    ) {
        this.qsar_preprocessingsteptypes = new ArrayList<>();
    }

    public qsar_PreprocessingType(
        ArrayList<qsar_PreprocessingStepType> qsar_preprocessingsteptypes    ) {
        this.qsar_preprocessingsteptypes = qsar_preprocessingsteptypes;
    }


    public List<qsar_PreprocessingStepType> getQsar_preprocessingsteptypes() {
        return qsar_preprocessingsteptypes;
    }

    public void addQsar_preprocessingsteptype(Qsar_preprocessingsteptype qsar_preprocessingsteptype) {
        this.qsar_preprocessingsteptypes.add(qsar_preprocessingsteptype);
    }
    public qsar_QsarType getQsar_qsartype() {
        return qsar_qsartype;
    }

    public void setQsar_qsartype(qsar_QsarType qsar_qsartype) {
        this.qsar_qsartype = qsar_qsartype;
    }

}