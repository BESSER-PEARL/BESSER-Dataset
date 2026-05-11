





import java.util.List;
import java.util.ArrayList;

public class Maude_OpTypedMapping extends RenMapping {

    private String to;
    private String atts;





    private Maude_Operation maude_operation;


    public Maude_OpTypedMapping(
        String to,        String atts    ) {
        super(
        );
        this.to = to;
        this.atts = atts;
    }


    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public String getAtts() {
        return atts;
    }

    public void setAtts(String atts) {
        this.atts = atts;
    }

    public Maude_Operation getMaude_operation() {
        return maude_operation;
    }

    public void setMaude_operation(Maude_Operation maude_operation) {
        this.maude_operation = maude_operation;
    }

}