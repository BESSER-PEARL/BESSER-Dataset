





import java.util.List;
import java.util.ArrayList;

public class moba_MobaBluetoothModule extends MobaExternalModule {

    private String type;



    public moba_MobaBluetoothModule(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}