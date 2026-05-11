





import java.util.List;
import java.util.ArrayList;

public class alf_CompoundAcceptStatementCompletion  {






    private alf_AcceptStatement alf_acceptstatement;




    private alf_Block alf_block;




    private List<alf_AcceptBlock> alf_acceptblocks;


    public alf_CompoundAcceptStatementCompletion(
    ) {
        this.alf_acceptblocks = new ArrayList<>();
    }

    public alf_CompoundAcceptStatementCompletion(
        ArrayList<alf_AcceptBlock> alf_acceptblocks    ) {
        this.alf_acceptblocks = alf_acceptblocks;
    }


    public alf_AcceptStatement getAlf_acceptstatement() {
        return alf_acceptstatement;
    }

    public void setAlf_acceptstatement(alf_AcceptStatement alf_acceptstatement) {
        this.alf_acceptstatement = alf_acceptstatement;
    }
    public alf_Block getAlf_block() {
        return alf_block;
    }

    public void setAlf_block(alf_Block alf_block) {
        this.alf_block = alf_block;
    }
    public List<alf_AcceptBlock> getAlf_acceptblocks() {
        return alf_acceptblocks;
    }

    public void addAlf_acceptblock(Alf_acceptblock alf_acceptblock) {
        this.alf_acceptblocks.add(alf_acceptblock);
    }

}