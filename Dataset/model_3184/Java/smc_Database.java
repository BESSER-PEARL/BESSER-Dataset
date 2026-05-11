





import java.util.List;
import java.util.ArrayList;

public class smc_Database extends Download {

    private String clm;





    private smc_Expression smc_expression;


    public smc_Database(
        String clm    ) {
        super(
        );
        this.clm = clm;
    }


    public String getClm() {
        return clm;
    }

    public void setClm(String clm) {
        this.clm = clm;
    }

    public smc_Expression getSmc_expression() {
        return smc_expression;
    }

    public void setSmc_expression(smc_Expression smc_expression) {
        this.smc_expression = smc_expression;
    }

}