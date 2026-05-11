





import java.util.List;
import java.util.ArrayList;

public class micro_Attribute  {

    private boolean isId;
    private boolean isGenerated;
    private boolean isMany;
    private String name;





    private micro_Model micro_model;




    private micro_Model micro_model;


    public micro_Attribute(
        boolean isId,        boolean isGenerated,        boolean isMany,        String name    ) {
        this.isId = isId;
        this.isGenerated = isGenerated;
        this.isMany = isMany;
        this.name = name;
    }


    public boolean getIsid() {
        return isId;
    }

    public void setIsid(boolean isId) {
        this.isId = isId;
    }
    public boolean getIsgenerated() {
        return isGenerated;
    }

    public void setIsgenerated(boolean isGenerated) {
        this.isGenerated = isGenerated;
    }
    public boolean getIsmany() {
        return isMany;
    }

    public void setIsmany(boolean isMany) {
        this.isMany = isMany;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public micro_Model getMicro_model() {
        return micro_model;
    }

    public void setMicro_model(micro_Model micro_model) {
        this.micro_model = micro_model;
    }
    public micro_Model getMicro_model() {
        return micro_model;
    }

    public void setMicro_model(micro_Model micro_model) {
        this.micro_model = micro_model;
    }

}