





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_VarParameter extends Variable, Parameter {

    private String kind;



    public QVTOperational_VarParameter(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}