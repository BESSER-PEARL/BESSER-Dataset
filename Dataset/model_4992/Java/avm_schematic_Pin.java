





import java.util.List;
import java.util.ArrayList;

public class avm_schematic_Pin extends DomainModelPort {

    private String EDASymbolRotation;
    private String EDASymbolLocationX;
    private String SPICEPortNumber;
    private String EDAGate;
    private String EDASymbolLocationY;



    public avm_schematic_Pin(
        String EDASymbolRotation,        String EDASymbolLocationX,        String SPICEPortNumber,        String EDAGate,        String EDASymbolLocationY    ) {
        super(
        );
        this.EDASymbolRotation = EDASymbolRotation;
        this.EDASymbolLocationX = EDASymbolLocationX;
        this.SPICEPortNumber = SPICEPortNumber;
        this.EDAGate = EDAGate;
        this.EDASymbolLocationY = EDASymbolLocationY;
    }


    public String getEdasymbolrotation() {
        return EDASymbolRotation;
    }

    public void setEdasymbolrotation(String EDASymbolRotation) {
        this.EDASymbolRotation = EDASymbolRotation;
    }
    public String getEdasymbollocationx() {
        return EDASymbolLocationX;
    }

    public void setEdasymbollocationx(String EDASymbolLocationX) {
        this.EDASymbolLocationX = EDASymbolLocationX;
    }
    public String getSpiceportnumber() {
        return SPICEPortNumber;
    }

    public void setSpiceportnumber(String SPICEPortNumber) {
        this.SPICEPortNumber = SPICEPortNumber;
    }
    public String getEdagate() {
        return EDAGate;
    }

    public void setEdagate(String EDAGate) {
        this.EDAGate = EDAGate;
    }
    public String getEdasymbollocationy() {
        return EDASymbolLocationY;
    }

    public void setEdasymbollocationy(String EDASymbolLocationY) {
        this.EDASymbolLocationY = EDASymbolLocationY;
    }


}