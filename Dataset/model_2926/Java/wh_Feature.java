





import java.util.List;
import java.util.ArrayList;

public class wh_Feature  {

    private String name;
    private boolean many;





    private wh_Entity wh_entity;




    private wh_Type wh_type;


    public wh_Feature(
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

    public wh_Entity getWh_entity() {
        return wh_entity;
    }

    public void setWh_entity(wh_Entity wh_entity) {
        this.wh_entity = wh_entity;
    }
    public wh_Type getWh_type() {
        return wh_type;
    }

    public void setWh_type(wh_Type wh_type) {
        this.wh_type = wh_type;
    }

}