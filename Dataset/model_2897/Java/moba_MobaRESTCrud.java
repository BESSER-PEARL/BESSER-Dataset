





import java.util.List;
import java.util.ArrayList;

public class moba_MobaRESTCrud extends MobaREST {

    private String operations;





    private moba_MobaRESTCrud moba_mobarestcrud;


    public moba_MobaRESTCrud(
        String operations    ) {
        super(
        );
        this.operations = operations;
    }


    public String getOperations() {
        return operations;
    }

    public void setOperations(String operations) {
        this.operations = operations;
    }

    public moba_MobaRESTCrud getMoba_mobarestcrud() {
        return moba_mobarestcrud;
    }

    public void setMoba_mobarestcrud(moba_MobaRESTCrud moba_mobarestcrud) {
        this.moba_mobarestcrud = moba_mobarestcrud;
    }

}