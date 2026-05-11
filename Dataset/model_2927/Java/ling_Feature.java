





import java.util.List;
import java.util.ArrayList;

public class ling_Feature  {

    private String name;
    private boolean many;





    private ling_Type ling_type;




    private ling_Entity ling_entity;


    public ling_Feature(
        String name,        boolean many    ) {
        this.name = name;
        this.many = many;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }

    public ling_Type getLing_type() {
        return ling_type;
    }

    public void setLing_type(ling_Type ling_type) {
        this.ling_type = ling_type;
    }
    public ling_Entity getLing_entity() {
        return ling_entity;
    }

    public void setLing_entity(ling_Entity ling_entity) {
        this.ling_entity = ling_entity;
    }

}