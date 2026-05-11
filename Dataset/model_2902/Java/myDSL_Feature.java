





import java.util.List;
import java.util.ArrayList;

public class myDSL_Feature extends NamedElement {

    private String kind;





    private myDSL_Type mydsl_type;


    public myDSL_Feature(
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

    public myDSL_Type getMydsl_type() {
        return mydsl_type;
    }

    public void setMydsl_type(myDSL_Type mydsl_type) {
        this.mydsl_type = mydsl_type;
    }

}