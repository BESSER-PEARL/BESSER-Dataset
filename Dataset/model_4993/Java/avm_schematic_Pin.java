





import java.util.List;
import java.util.ArrayList;

public class avm_schematic_Pin extends DomainModelPort {

    private String EDAGate;
    private String EDASymbolLocationX;
    private String EDASymbolRotation;
    private String SPICEPortNumber;
    private String EDASymbolLocationY;



    public avm_schematic_Pin(
        String EDAGate,        String EDASymbolLocationX,        String EDASymbolRotation,        String SPICEPortNumber,        String EDASymbolLocationY    ) {
        super(
        );
        this.EDAGate = EDAGate;
        this.EDASymbolLocationX = EDASymbolLocationX;
        this.EDASymbolRotation = EDASymbolRotation;
        this.SPICEPortNumber = SPICEPortNumber;
        this.EDASymbolLocationY = EDASymbolLocationY;
    }


    public String getEdagate() {
        return EDAGate;
    }

    public void setEdagate(String EDAGate) {
        this.EDAGate = EDAGate;
    }
    public String getEdasymbollocationx() {
        return EDASymbolLocationX;
    }

    public void setEdasymbollocationx(String EDASymbolLocationX) {
        this.EDASymbolLocationX = EDASymbolLocationX;
    }
    public String getEdasymbolrotation() {
        return EDASymbolRotation;
    }

    public void setEdasymbolrotation(String EDASymbolRotation) {
        this.EDASymbolRotation = EDASymbolRotation;
    }
    public String getSpiceportnumber() {
        return SPICEPortNumber;
    }

    public void setSpiceportnumber(String SPICEPortNumber) {
        this.SPICEPortNumber = SPICEPortNumber;
    }
    public String getEdasymbollocationy() {
        return EDASymbolLocationY;
    }

    public void setEdasymbollocationy(String EDASymbolLocationY) {
        this.EDASymbolLocationY = EDASymbolLocationY;
    }


}