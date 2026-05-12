





import java.util.List;
import java.util.ArrayList;

public class SQLDML_OperationExp extends BinaryExp {

    private String optName;



    public SQLDML_OperationExp(
        String optName    ) {
        super(
        );
        this.optName = optName;
    }


    public String getOptname() {
        return optName;
    }

    public void setOptname(String optName) {
        this.optName = optName;
    }


}