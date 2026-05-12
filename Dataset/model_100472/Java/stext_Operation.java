





import java.util.List;
import java.util.ArrayList;

public class stext_Operation extends Declaration {






    private stext_OperationCall stext_operationcall;




    private stext_Type stext_type;




    private List<stext_Type> stext_types;


    public stext_Operation(
    ) {
        super(
        );
        this.stext_types = new ArrayList<>();
    }

    public stext_Operation(
        ArrayList<stext_Type> stext_types    ) {
        this.stext_types = stext_types;
    }


    public stext_OperationCall getStext_operationcall() {
        return stext_operationcall;
    }

    public void setStext_operationcall(stext_OperationCall stext_operationcall) {
        this.stext_operationcall = stext_operationcall;
    }
    public stext_Type getStext_type() {
        return stext_type;
    }

    public void setStext_type(stext_Type stext_type) {
        this.stext_type = stext_type;
    }
    public List<stext_Type> getStext_types() {
        return stext_types;
    }

    public void addStext_type(Stext_type stext_type) {
        this.stext_types.add(stext_type);
    }

}