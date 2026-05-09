





import java.util.List;
import java.util.ArrayList;

public class simpleworld101_Part extends Named {

    private int id;
    private String content;





    private simpleworld101_Thing simpleworld101_thing;




    private simpleworld101_Relations simpleworld101_relations;


    public simpleworld101_Part(
        int id,        String content    ) {
        super(
        );
        this.id = id;
        this.content = content;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public simpleworld101_Thing getSimpleworld101_thing() {
        return simpleworld101_thing;
    }

    public void setSimpleworld101_thing(simpleworld101_Thing simpleworld101_thing) {
        this.simpleworld101_thing = simpleworld101_thing;
    }
    public simpleworld101_Relations getSimpleworld101_relations() {
        return simpleworld101_relations;
    }

    public void setSimpleworld101_relations(simpleworld101_Relations simpleworld101_relations) {
        this.simpleworld101_relations = simpleworld101_relations;
    }

}