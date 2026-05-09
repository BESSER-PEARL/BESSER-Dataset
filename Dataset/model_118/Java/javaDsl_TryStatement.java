





import java.util.List;
import java.util.ArrayList;

public class javaDsl_TryStatement extends Statement {






    private javaDsl_Block javadsl_block;




    private javaDsl_Block javadsl_block;




    private List<javaDsl_FormalParameter> javadsl_formalparameters;




    private List<javaDsl_Block> javadsl_blocks;


    public javaDsl_TryStatement(
    ) {
        super(
        );
        this.javadsl_formalparameters = new ArrayList<>();
        this.javadsl_blocks = new ArrayList<>();
    }

    public javaDsl_TryStatement(
        ArrayList<javaDsl_FormalParameter> javadsl_formalparameters,        ArrayList<javaDsl_Block> javadsl_blocks    ) {
        this.javadsl_formalparameters = javadsl_formalparameters;
        this.javadsl_blocks = javadsl_blocks;
    }


    public javaDsl_Block getJavadsl_block() {
        return javadsl_block;
    }

    public void setJavadsl_block(javaDsl_Block javadsl_block) {
        this.javadsl_block = javadsl_block;
    }
    public javaDsl_Block getJavadsl_block() {
        return javadsl_block;
    }

    public void setJavadsl_block(javaDsl_Block javadsl_block) {
        this.javadsl_block = javadsl_block;
    }
    public List<javaDsl_FormalParameter> getJavadsl_formalparameters() {
        return javadsl_formalparameters;
    }

    public void addJavadsl_formalparameter(Javadsl_formalparameter javadsl_formalparameter) {
        this.javadsl_formalparameters.add(javadsl_formalparameter);
    }
    public List<javaDsl_Block> getJavadsl_blocks() {
        return javadsl_blocks;
    }

    public void addJavadsl_block(Javadsl_block javadsl_block) {
        this.javadsl_blocks.add(javadsl_block);
    }

}