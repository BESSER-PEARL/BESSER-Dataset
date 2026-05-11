





import java.util.List;
import java.util.ArrayList;

public class siddhi_ExecPartition extends PARTITION, BEGIN, WITH, END {






    private siddhi_ExecutionElement siddhi_executionelement;


    public siddhi_ExecPartition(
    ) {
        super(
        );
    }



    public siddhi_ExecutionElement getSiddhi_executionelement() {
        return siddhi_executionelement;
    }

    public void setSiddhi_executionelement(siddhi_ExecutionElement siddhi_executionelement) {
        this.siddhi_executionelement = siddhi_executionelement;
    }

}