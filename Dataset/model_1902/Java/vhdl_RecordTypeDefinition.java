





import java.util.List;
import java.util.ArrayList;

public class vhdl_RecordTypeDefinition extends CompositeTypeDefinition {






    private List<vhdl_RecordField> vhdl_recordfields;




    private List<vhdl_SubtypeIndication> vhdl_subtypeindications;


    public vhdl_RecordTypeDefinition(
    ) {
        super(
        );
        this.vhdl_recordfields = new ArrayList<>();
        this.vhdl_subtypeindications = new ArrayList<>();
    }

    public vhdl_RecordTypeDefinition(
        ArrayList<vhdl_RecordField> vhdl_recordfields,        ArrayList<vhdl_SubtypeIndication> vhdl_subtypeindications    ) {
        this.vhdl_recordfields = vhdl_recordfields;
        this.vhdl_subtypeindications = vhdl_subtypeindications;
    }


    public List<vhdl_RecordField> getVhdl_recordfields() {
        return vhdl_recordfields;
    }

    public void addVhdl_recordfield(Vhdl_recordfield vhdl_recordfield) {
        this.vhdl_recordfields.add(vhdl_recordfield);
    }
    public List<vhdl_SubtypeIndication> getVhdl_subtypeindications() {
        return vhdl_subtypeindications;
    }

    public void addVhdl_subtypeindication(Vhdl_subtypeindication vhdl_subtypeindication) {
        this.vhdl_subtypeindications.add(vhdl_subtypeindication);
    }

}