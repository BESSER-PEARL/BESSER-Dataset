





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwRegister_HwRegister extends HwMemory {

    private String address;



    public MARTE_HwRegister_HwRegister(
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


}