





import java.util.List;
import java.util.ArrayList;

public class ir_EFEnumLiteral  {

    private String name;





    private ir_EFEnum ir_efenum;


    public ir_EFEnumLiteral(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ir_EFEnum getIr_efenum() {
        return ir_efenum;
    }

    public void setIr_efenum(ir_EFEnum ir_efenum) {
        this.ir_efenum = ir_efenum;
    }

}