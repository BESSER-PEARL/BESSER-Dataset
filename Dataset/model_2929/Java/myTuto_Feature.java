





import java.util.List;
import java.util.ArrayList;

public class myTuto_Feature  {

    private String name;
    private boolean many;





    private myTuto_Type mytuto_type;




    private myTuto_Entity mytuto_entity;


    public myTuto_Feature(
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

    public myTuto_Type getMytuto_type() {
        return mytuto_type;
    }

    public void setMytuto_type(myTuto_Type mytuto_type) {
        this.mytuto_type = mytuto_type;
    }
    public myTuto_Entity getMytuto_entity() {
        return mytuto_entity;
    }

    public void setMytuto_entity(myTuto_Entity mytuto_entity) {
        this.mytuto_entity = mytuto_entity;
    }

}