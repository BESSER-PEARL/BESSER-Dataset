





import java.util.List;
import java.util.ArrayList;

public class vhdl_IfStatement extends SequentialStatement {

    private String label;





    private List<vhdl_SequentialStatement> vhdl_sequentialstatements;


    public vhdl_IfStatement(
        String label    ) {
        super(
        );
        this.label = label;
        this.vhdl_sequentialstatements = new ArrayList<>();
    }

    public vhdl_IfStatement(
        String label        ArrayList<vhdl_SequentialStatement> vhdl_sequentialstatements    ) {
        this.label = label;
        this.vhdl_sequentialstatements = vhdl_sequentialstatements;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<vhdl_SequentialStatement> getVhdl_sequentialstatements() {
        return vhdl_sequentialstatements;
    }

    public void addVhdl_sequentialstatement(Vhdl_sequentialstatement vhdl_sequentialstatement) {
        this.vhdl_sequentialstatements.add(vhdl_sequentialstatement);
    }

}