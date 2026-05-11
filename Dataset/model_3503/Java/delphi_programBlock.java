





import java.util.List;
import java.util.ArrayList;

public class delphi_programBlock extends CSTrace {






    private delphi_usesClause delphi_usesclause;




    private delphi_library delphi_library;




    private delphi_block delphi_block;




    private delphi_program delphi_program;


    public delphi_programBlock(
    ) {
        super(
        );
    }



    public delphi_usesClause getDelphi_usesclause() {
        return delphi_usesclause;
    }

    public void setDelphi_usesclause(delphi_usesClause delphi_usesclause) {
        this.delphi_usesclause = delphi_usesclause;
    }
    public delphi_library getDelphi_library() {
        return delphi_library;
    }

    public void setDelphi_library(delphi_library delphi_library) {
        this.delphi_library = delphi_library;
    }
    public delphi_block getDelphi_block() {
        return delphi_block;
    }

    public void setDelphi_block(delphi_block delphi_block) {
        this.delphi_block = delphi_block;
    }
    public delphi_program getDelphi_program() {
        return delphi_program;
    }

    public void setDelphi_program(delphi_program delphi_program) {
        this.delphi_program = delphi_program;
    }

}