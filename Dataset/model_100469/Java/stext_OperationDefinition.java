





import java.util.List;
import java.util.ArrayList;

public class stext_OperationDefinition extends Declaration, Operation {






    private List<stext_Type> stext_types;


    public stext_OperationDefinition(
    ) {
        super(
        );
        this.stext_types = new ArrayList<>();
    }

    public stext_OperationDefinition(
        ArrayList<stext_Type> stext_types    ) {
        this.stext_types = stext_types;
    }


    public List<stext_Type> getStext_types() {
        return stext_types;
    }

    public void addStext_type(Stext_type stext_type) {
        this.stext_types.add(stext_type);
    }

}