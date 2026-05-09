





import java.util.List;
import java.util.ArrayList;

public class oCLlite_TuplePart  {

    private String name;





    private oCLlite_TupleExp ocllite_tupleexp;




    private oCLlite_OclLExpression ocllite_ocllexpression;




    private oCLlite_OclLType ocllite_oclltype;


    public oCLlite_TuplePart(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public oCLlite_TupleExp getOcllite_tupleexp() {
        return ocllite_tupleexp;
    }

    public void setOcllite_tupleexp(oCLlite_TupleExp ocllite_tupleexp) {
        this.ocllite_tupleexp = ocllite_tupleexp;
    }
    public oCLlite_OclLExpression getOcllite_ocllexpression() {
        return ocllite_ocllexpression;
    }

    public void setOcllite_ocllexpression(oCLlite_OclLExpression ocllite_ocllexpression) {
        this.ocllite_ocllexpression = ocllite_ocllexpression;
    }
    public oCLlite_OclLType getOcllite_oclltype() {
        return ocllite_oclltype;
    }

    public void setOcllite_oclltype(oCLlite_OclLType ocllite_oclltype) {
        this.ocllite_oclltype = ocllite_oclltype;
    }

}