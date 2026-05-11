





import java.util.List;
import java.util.ArrayList;

public class dom_QueryOperation extends DaoOperation, IDocumentable {






    private dom_Dao dom_dao;


    public dom_QueryOperation(
    ) {
        super(
        );
    }



    public dom_Dao getDom_dao() {
        return dom_dao;
    }

    public void setDom_dao(dom_Dao dom_dao) {
        this.dom_dao = dom_dao;
    }

}