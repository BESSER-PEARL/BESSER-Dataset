





import java.util.List;
import java.util.ArrayList;

public class avm_Operand  {

    private String Symbol;





    private avm_ComplexFormula avm_complexformula;




    private avm_ValueNode avm_valuenode;


    public avm_Operand(
        String Symbol    ) {
        this.Symbol = Symbol;
    }


    public String getSymbol() {
        return Symbol;
    }

    public void setSymbol(String Symbol) {
        this.Symbol = Symbol;
    }

    public avm_ComplexFormula getAvm_complexformula() {
        return avm_complexformula;
    }

    public void setAvm_complexformula(avm_ComplexFormula avm_complexformula) {
        this.avm_complexformula = avm_complexformula;
    }
    public avm_ValueNode getAvm_valuenode() {
        return avm_valuenode;
    }

    public void setAvm_valuenode(avm_ValueNode avm_valuenode) {
        this.avm_valuenode = avm_valuenode;
    }

}