





import java.util.List;
import java.util.ArrayList;

public class dom_DaoOperation  {

    private String name;
    private boolean many;





    private dom_DelegateOperation dom_delegateoperation;


    public dom_DaoOperation(
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

    public dom_DelegateOperation getDom_delegateoperation() {
        return dom_delegateoperation;
    }

    public void setDom_delegateoperation(dom_DelegateOperation dom_delegateoperation) {
        this.dom_delegateoperation = dom_delegateoperation;
    }

}