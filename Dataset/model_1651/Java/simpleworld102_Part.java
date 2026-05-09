





import java.util.List;
import java.util.ArrayList;

public class simpleworld102_Part extends Named {

    private int id;
    private String content;





    private simpleworld102_Thing simpleworld102_thing;




    private simpleworld102_Relations simpleworld102_relations;


    public simpleworld102_Part(
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

    public simpleworld102_Thing getSimpleworld102_thing() {
        return simpleworld102_thing;
    }

    public void setSimpleworld102_thing(simpleworld102_Thing simpleworld102_thing) {
        this.simpleworld102_thing = simpleworld102_thing;
    }
    public simpleworld102_Relations getSimpleworld102_relations() {
        return simpleworld102_relations;
    }

    public void setSimpleworld102_relations(simpleworld102_Relations simpleworld102_relations) {
        this.simpleworld102_relations = simpleworld102_relations;
    }

}