





import java.util.List;
import java.util.ArrayList;

public class ir_ItemIndexDefinition extends Instruction {






    private ir_ItemIndex ir_itemindex;




    private ir_ItemIndexValue ir_itemindexvalue;


    public ir_ItemIndexDefinition(
    ) {
        super(
        );
    }



    public ir_ItemIndex getIr_itemindex() {
        return ir_itemindex;
    }

    public void setIr_itemindex(ir_ItemIndex ir_itemindex) {
        this.ir_itemindex = ir_itemindex;
    }
    public ir_ItemIndexValue getIr_itemindexvalue() {
        return ir_itemindexvalue;
    }

    public void setIr_itemindexvalue(ir_ItemIndexValue ir_itemindexvalue) {
        this.ir_itemindexvalue = ir_itemindexvalue;
    }

}