





import java.util.List;
import java.util.ArrayList;

public class drn_Declaration  {

    private String name;
    private String typePrimitif;





    private drn_TypeGeneric drn_typegeneric;




    private drn_Device drn_device;


    public drn_Declaration(
        String name,        String typePrimitif    ) {
        this.name = name;
        this.typePrimitif = typePrimitif;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTypeprimitif() {
        return typePrimitif;
    }

    public void setTypeprimitif(String typePrimitif) {
        this.typePrimitif = typePrimitif;
    }

    public drn_TypeGeneric getDrn_typegeneric() {
        return drn_typegeneric;
    }

    public void setDrn_typegeneric(drn_TypeGeneric drn_typegeneric) {
        this.drn_typegeneric = drn_typegeneric;
    }
    public drn_Device getDrn_device() {
        return drn_device;
    }

    public void setDrn_device(drn_Device drn_device) {
        this.drn_device = drn_device;
    }

}