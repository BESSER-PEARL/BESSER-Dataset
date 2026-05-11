





import java.util.List;
import java.util.ArrayList;

public class pimm_Delay extends Parameterizable {






    private pimm_Fifo pimm_fifo;




    private pimm_Expression pimm_expression;


    public pimm_Delay(
    ) {
        super(
        );
    }



    public pimm_Fifo getPimm_fifo() {
        return pimm_fifo;
    }

    public void setPimm_fifo(pimm_Fifo pimm_fifo) {
        this.pimm_fifo = pimm_fifo;
    }
    public pimm_Expression getPimm_expression() {
        return pimm_expression;
    }

    public void setPimm_expression(pimm_Expression pimm_expression) {
        this.pimm_expression = pimm_expression;
    }

}