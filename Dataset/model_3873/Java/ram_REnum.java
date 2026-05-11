





import java.util.List;
import java.util.ArrayList;

public class ram_REnum extends PrimitiveType {






    private List<ram_REnumLiteral> ram_renumliterals;




    private ram_REnumLiteral ram_renumliteral;


    public ram_REnum(
    ) {
        super(
        );
        this.ram_renumliterals = new ArrayList<>();
    }

    public ram_REnum(
        ArrayList<ram_REnumLiteral> ram_renumliterals    ) {
        this.ram_renumliterals = ram_renumliterals;
    }


    public List<ram_REnumLiteral> getRam_renumliterals() {
        return ram_renumliterals;
    }

    public void addRam_renumliteral(Ram_renumliteral ram_renumliteral) {
        this.ram_renumliterals.add(ram_renumliteral);
    }
    public ram_REnumLiteral getRam_renumliteral() {
        return ram_renumliteral;
    }

    public void setRam_renumliteral(ram_REnumLiteral ram_renumliteral) {
        this.ram_renumliteral = ram_renumliteral;
    }

}