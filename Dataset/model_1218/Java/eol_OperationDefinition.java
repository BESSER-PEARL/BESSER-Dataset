





import java.util.List;
import java.util.ArrayList;

public class eol_OperationDefinition extends EOLElement {






    private List<eol_OperationDefinition> eol_operationdefinitions;


    public eol_OperationDefinition(
    ) {
        super(
        );
        this.eol_operationdefinitions = new ArrayList<>();
    }

    public eol_OperationDefinition(
        ArrayList<eol_OperationDefinition> eol_operationdefinitions    ) {
        this.eol_operationdefinitions = eol_operationdefinitions;
    }


    public List<eol_OperationDefinition> getEol_operationdefinitions() {
        return eol_operationdefinitions;
    }

    public void addEol_operationdefinition(Eol_operationdefinition eol_operationdefinition) {
        this.eol_operationdefinitions.add(eol_operationdefinition);
    }

}