





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_VarParameter extends Variable, Parameter {

    private String kind;



    public qvtoperational_VarParameter(
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