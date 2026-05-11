





import java.util.List;
import java.util.ArrayList;

public class aGES_Feature  {

    private boolean many;
    private String name;





    private aGES_Type ages_type;




    private aGES_Entity ages_entity;


    public aGES_Feature(
        boolean many,        String name    ) {
        this.many = many;
        this.name = name;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public aGES_Type getAges_type() {
        return ages_type;
    }

    public void setAges_type(aGES_Type ages_type) {
        this.ages_type = ages_type;
    }
    public aGES_Entity getAges_entity() {
        return ages_entity;
    }

    public void setAges_entity(aGES_Entity ages_entity) {
        this.ages_entity = ages_entity;
    }

}