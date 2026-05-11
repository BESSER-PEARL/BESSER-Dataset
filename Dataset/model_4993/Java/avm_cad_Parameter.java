





import java.util.List;
import java.util.ArrayList;

public class avm_cad_Parameter extends DomainModelParameter {

    private String Name;



    public avm_cad_Parameter(
        String Name    ) {
        super(
        );
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}