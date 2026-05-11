





import java.util.List;
import java.util.ArrayList;

public class Maude_OpMapping extends RenMapping {

    private String to;





    private Maude_Operation maude_operation;


    public Maude_OpMapping(
        String to    ) {
        super(
        );
        this.to = to;
    }


    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }

    public Maude_Operation getMaude_operation() {
        return maude_operation;
    }

    public void setMaude_operation(Maude_Operation maude_operation) {
        this.maude_operation = maude_operation;
    }

}