





import java.util.List;
import java.util.ArrayList;

public class dom_Parameter extends QueryParameter, QueryParameterReference {

    private String name;
    private boolean many;



    public dom_Parameter(
        String name,        boolean many    ) {
        super(
        );
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


}