





import java.util.List;
import java.util.ArrayList;

public class mil_RegisterReference extends Value {

    private String address;





    private mil_StoreInstruction mil_storeinstruction;


    public mil_RegisterReference(
        String address    ) {
        super(
        );
        this.address = address;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public mil_StoreInstruction getMil_storeinstruction() {
        return mil_storeinstruction;
    }

    public void setMil_storeinstruction(mil_StoreInstruction mil_storeinstruction) {
        this.mil_storeinstruction = mil_storeinstruction;
    }

}