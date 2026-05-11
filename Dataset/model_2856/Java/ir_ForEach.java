





import java.util.List;
import java.util.ArrayList;

public class ir_ForEach extends Statement {






    private List<ir_Generator> ir_generators;




    private ir_Block ir_block;


    public ir_ForEach(
    ) {
        super(
        );
        this.ir_generators = new ArrayList<>();
    }

    public ir_ForEach(
        ArrayList<ir_Generator> ir_generators    ) {
        this.ir_generators = ir_generators;
    }


    public List<ir_Generator> getIr_generators() {
        return ir_generators;
    }

    public void addIr_generator(Ir_generator ir_generator) {
        this.ir_generators.add(ir_generator);
    }
    public ir_Block getIr_block() {
        return ir_block;
    }

    public void setIr_block(ir_Block ir_block) {
        this.ir_block = ir_block;
    }

}