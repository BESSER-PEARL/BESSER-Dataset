





import java.util.List;
import java.util.ArrayList;

public class moba_MobaRESTCustomService extends MobaREST {

    private String operation;





    private moba_MobaRESTCustomService moba_mobarestcustomservice;


    public moba_MobaRESTCustomService(
        String operation    ) {
        super(
        );
        this.operation = operation;
    }


    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public moba_MobaRESTCustomService getMoba_mobarestcustomservice() {
        return moba_mobarestcustomservice;
    }

    public void setMoba_mobarestcustomservice(moba_MobaRESTCustomService moba_mobarestcustomservice) {
        this.moba_mobarestcustomservice = moba_mobarestcustomservice;
    }

}