





import java.util.List;
import java.util.ArrayList;

public class ir_Iterator extends IterationBlock {






    private ir_ItemIndex ir_itemindex;




    private ir_SimpleVariable ir_simplevariable;




    private ir_Container ir_container;


    public ir_Iterator(
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
    public ir_SimpleVariable getIr_simplevariable() {
        return ir_simplevariable;
    }

    public void setIr_simplevariable(ir_SimpleVariable ir_simplevariable) {
        this.ir_simplevariable = ir_simplevariable;
    }
    public ir_Container getIr_container() {
        return ir_container;
    }

    public void setIr_container(ir_Container ir_container) {
        this.ir_container = ir_container;
    }

}