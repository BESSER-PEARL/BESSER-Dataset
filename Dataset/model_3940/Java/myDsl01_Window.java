





import java.util.List;
import java.util.ArrayList;

public class myDsl01_Window  {

    private String name;
    private String title;





    private myDsl01_Model mydsl01_model;




    private myDsl01_Entity mydsl01_entity;




    private myDsl01_Size mydsl01_size;


    public myDsl01_Window(
        String name,        String title    ) {
        this.name = name;
        this.title = title;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public myDsl01_Model getMydsl01_model() {
        return mydsl01_model;
    }

    public void setMydsl01_model(myDsl01_Model mydsl01_model) {
        this.mydsl01_model = mydsl01_model;
    }
    public myDsl01_Entity getMydsl01_entity() {
        return mydsl01_entity;
    }

    public void setMydsl01_entity(myDsl01_Entity mydsl01_entity) {
        this.mydsl01_entity = mydsl01_entity;
    }
    public myDsl01_Size getMydsl01_size() {
        return mydsl01_size;
    }

    public void setMydsl01_size(myDsl01_Size mydsl01_size) {
        this.mydsl01_size = mydsl01_size;
    }

}