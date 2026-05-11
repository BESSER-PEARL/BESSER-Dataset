





import java.util.List;
import java.util.ArrayList;

public class systemmodel_Block extends SMElement {

    private int sequenceNumber;





    private systemmodel_SystemModel systemmodel_systemmodel;


    public systemmodel_Block(
        int sequenceNumber    ) {
        super(
        );
        this.sequenceNumber = sequenceNumber;
    }


    public int getSequencenumber() {
        return sequenceNumber;
    }

    public void setSequencenumber(int sequenceNumber) {
        this.sequenceNumber = sequenceNumber;
    }

    public systemmodel_SystemModel getSystemmodel_systemmodel() {
        return systemmodel_systemmodel;
    }

    public void setSystemmodel_systemmodel(systemmodel_SystemModel systemmodel_systemmodel) {
        this.systemmodel_systemmodel = systemmodel_systemmodel;
    }

}