





import java.util.List;
import java.util.ArrayList;

public class SQL2003_BehaviouralComponent  {

    private String name;
    private String body;



    public SQL2003_BehaviouralComponent(
        String name,        String body    ) {
        this.name = name;
        this.body = body;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }


}