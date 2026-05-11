





import java.util.List;
import java.util.ArrayList;

public class avm_systemc_SystemCModel extends DomainModel_ {

    private String ModuleName;



    public avm_systemc_SystemCModel(
        String ModuleName    ) {
        super(
        );
        this.ModuleName = ModuleName;
    }


    public String getModulename() {
        return ModuleName;
    }

    public void setModulename(String ModuleName) {
        this.ModuleName = ModuleName;
    }


}