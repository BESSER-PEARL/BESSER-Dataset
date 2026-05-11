





import java.util.List;
import java.util.ArrayList;

public class vhdl_statement_Statement extends VhdlObject {

    private String label;



    public vhdl_statement_Statement(
        String label    ) {
        super(
        );
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}