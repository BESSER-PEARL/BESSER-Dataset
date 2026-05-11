





import java.util.List;
import java.util.ArrayList;

public class dom_DelegateOperation extends IDocumentable {

    private boolean many;
    private String crudOperationType;
    private String name;





    private dom_Dao dom_dao;




    private dom_Service dom_service;




    private dom_Operation dom_operation;


    public dom_DelegateOperation(
        boolean many,        String crudOperationType,        String name    ) {
        super(
        );
        this.many = many;
        this.crudOperationType = crudOperationType;
        this.name = name;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public String getCrudoperationtype() {
        return crudOperationType;
    }

    public void setCrudoperationtype(String crudOperationType) {
        this.crudOperationType = crudOperationType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dom_Dao getDom_dao() {
        return dom_dao;
    }

    public void setDom_dao(dom_Dao dom_dao) {
        this.dom_dao = dom_dao;
    }
    public dom_Service getDom_service() {
        return dom_service;
    }

    public void setDom_service(dom_Service dom_service) {
        this.dom_service = dom_service;
    }
    public dom_Operation getDom_operation() {
        return dom_operation;
    }

    public void setDom_operation(dom_Operation dom_operation) {
        this.dom_operation = dom_operation;
    }

}