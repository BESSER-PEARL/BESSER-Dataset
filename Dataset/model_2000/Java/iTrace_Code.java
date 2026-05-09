





import java.util.List;
import java.util.ArrayList;

public class iTrace_Code extends Artefact {






    private iTrace_Block itrace_block;




    private List<iTrace_Block> itrace_blocks;


    public iTrace_Code(
    ) {
        super(
        );
        this.itrace_blocks = new ArrayList<>();
    }

    public iTrace_Code(
        ArrayList<iTrace_Block> itrace_blocks    ) {
        this.itrace_blocks = itrace_blocks;
    }


    public iTrace_Block getItrace_block() {
        return itrace_block;
    }

    public void setItrace_block(iTrace_Block itrace_block) {
        this.itrace_block = itrace_block;
    }
    public List<iTrace_Block> getItrace_blocks() {
        return itrace_blocks;
    }

    public void addItrace_block(Itrace_block itrace_block) {
        this.itrace_blocks.add(itrace_block);
    }

}