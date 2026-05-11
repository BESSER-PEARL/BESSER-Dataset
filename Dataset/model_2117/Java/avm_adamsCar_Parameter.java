





import java.util.List;
import java.util.ArrayList;

public class avm_adamsCar_Parameter extends DomainModelParameter {

    private String Name;
    private String ID;



    public avm_adamsCar_Parameter(
        String Name,        String ID    ) {
        super(
        );
        this.Name = Name;
        this.ID = ID;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }


}