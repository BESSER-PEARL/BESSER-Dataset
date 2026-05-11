





import java.util.List;
import java.util.ArrayList;

public class dom_JoinEntity  {

    private String name;





    private dom_Join dom_join;


    public dom_JoinEntity(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dom_Join getDom_join() {
        return dom_join;
    }

    public void setDom_join(dom_Join dom_join) {
        this.dom_join = dom_join;
    }

}