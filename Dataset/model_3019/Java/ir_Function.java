





import java.util.List;
import java.util.ArrayList;

public class ir_Function extends IrAnnotable {

    private String name;
    private String provider;





    private ir_Instruction ir_instruction;


    public ir_Function(
        String name,        String provider    ) {
        super(
        );
        this.name = name;
        this.provider = provider;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }

    public ir_Instruction getIr_instruction() {
        return ir_instruction;
    }

    public void setIr_instruction(ir_Instruction ir_instruction) {
        this.ir_instruction = ir_instruction;
    }

}