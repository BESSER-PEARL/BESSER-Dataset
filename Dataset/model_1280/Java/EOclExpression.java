





import java.util.List;
import java.util.ArrayList;

public class EOclExpression  {






    private ocl_exp_ELoopExp ocl_exp_eloopexp;




    private ocl_exp_ECallExp ocl_exp_ecallexp;


    public EOclExpression(
    ) {
    }



    public ocl_exp_ELoopExp getOcl_exp_eloopexp() {
        return ocl_exp_eloopexp;
    }

    public void setOcl_exp_eloopexp(ocl_exp_ELoopExp ocl_exp_eloopexp) {
        this.ocl_exp_eloopexp = ocl_exp_eloopexp;
    }
    public ocl_exp_ECallExp getOcl_exp_ecallexp() {
        return ocl_exp_ecallexp;
    }

    public void setOcl_exp_ecallexp(ocl_exp_ECallExp ocl_exp_ecallexp) {
        this.ocl_exp_ecallexp = ocl_exp_ecallexp;
    }

}